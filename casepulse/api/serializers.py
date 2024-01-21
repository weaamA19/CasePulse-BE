from rest_framework import serializers
from .models import Case, Lawyer, Document, Reminder

# class LawyerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lawyer
#         fields =['firstName','lastName','userName', 'phoneNumber', 'email', 'password'] 
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['case_id','title','description', 'date']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['case_id','title','description', 'file_path']


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['title','description', 'status', 'clientCPR', 'clientEmail', 'case_start_date', 'case_end_date']