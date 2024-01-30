from rest_framework import serializers
from .models import Case, Lawyer, Document, Reminder
from django.contrib.auth import get_user_model

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['title','description', 'status', 'clientCPR', 'clientEmail', 'case_start_date', 'case_end_date']
   
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = instance.id
        return rep

class LawyerSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    cases = CaseSerializer(many=True, read_only=True)
    class Meta:
        model = Lawyer
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    # Nested serializer for the case_id field
    case_id = serializers.SerializerMethodField()  
    class Meta:
        model = Reminder
        fields = ['case_id','title','description', 'datetime', 'created_at', 'updated_at']
        read_only_fields = ['case_id']

    def get_case_id(self, obj):
        return self.context.get('case_id', None)  
    
    def create(self, validated_data):
        case_id = self.get_case_id(self.context)
        validated_data['case_id_id'] = case_id
        return super().create(validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = instance.id
        return rep



class TodayReminderSerializer(serializers.ModelSerializer):
    case_id = serializers.SerializerMethodField()  
    class Meta:
        model = Reminder
        fields = ['case_id','title','description', 'datetime', 'created_at', 'updated_at']
        read_only_fields = ['case_id']
    
    def get_case_id(self, obj):
        reminder_id = obj.id
        reminder_case_ids = self.context.get('reminder_case_ids', {})
        return reminder_case_ids.get(reminder_id, None)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = instance.id
        return rep
     
class DocumentSerializer(serializers.ModelSerializer):
    case_id = serializers.SerializerMethodField()  

    class Meta:
        model = Document
        fields = ['case_id', 'title', 'description', 'file_path', 'created_at', 'updated_at']
        read_only_fields = ['case_id']

    def get_case_id(self, obj):
        return self.context.get('case_id', None)  
    
    def create(self, validated_data):
        case_id = self.get_case_id(self.context)
        validated_data['case_id_id'] = case_id
        return super().create(validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = instance.id
        return rep
    

   
    # def create(self, validated_data):
    #     case_id = self.context['view'].kwargs['pk']
    #     case = Case.objects.get(pk=case_id)
    #     validated_data['case_id'] = case_id
    #     return super().create(validated_data)

class RegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'avatar')
        # extra_kwargs = {'password': {'write_only': True}}\

# the following are new code for adding the avatar
    def create(self, validated_data):
        avatar = validated_data.pop('avatar', None)
        user = super().create(validated_data)

        # Handle avatar field if provided
        if avatar:
            user.avatar = avatar
            user.save()
        return user


# class OldPasswordVerificationSerializer(serializers.Serializer):
#     old_password = serializers.CharField(max_length=128)
