from rest_framework import serializers
from .models import Case, Lawyer, Document, Reminder
from django.contrib.auth import get_user_model

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['title','description', 'status', 'clientCPR', 'clientEmail', 'case_start_date', 'case_end_date']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields ='__all__' 

class LawyerSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    cases = CaseSerializer(many=True, read_only=True)
    class Meta:
        model = Lawyer
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    # Nested serializer for the case_id field
    case_id = CaseSerializer()
    class Meta:
        model = Reminder
        fields = ['case_id','title','description', 'date']
    
class DocumentSerializer(serializers.ModelSerializer):
    # Nested serializer for the case_id field
    case_id = CaseSerializer()
    class Meta:
        model = Document
        fields = ['case_id','title','description', 'file_path']



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