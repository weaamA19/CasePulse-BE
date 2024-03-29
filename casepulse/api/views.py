from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone

from .models import Case, Lawyer, Document, Reminder
from django.core import serializers
from .serializers import *
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

# from rest_framework import permissions
# from rest_framework.decorators import permission_classes
# from django.contrib.auth.decorators import login_required

#################################Users API'S#################################
class RegistrationView(generics.CreateAPIView):
    serializer_class = RegisterationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.first_name = self.request.data.get('first_name')
        user.last_name = self.request.data.get('last_name')
        user.phone_number = self.request.data.get('phone_number')
        user.email = self.request.data.get('email')
        user.avatar = self.request.data.get('avatar')

        user.save()


# class OldPasswordVerificationView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         serializer = OldPasswordVerificationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = request.user
#         old_password = serializer.validated_data['old_password']

#         # Check if the old password is correct
#         if not authenticate(username=user.username, password=old_password):
#             return Response({'error': 'Incorrect old password'}, status=status.HTTP_400_BAD_REQUEST)

#         return Response({'message': 'Old password is correct'}, status=status.HTTP_200_OK)
class LawyersList(generics.ListAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer

class LawyersDetail(generics.RetrieveAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer

class LawyersUpdateOne(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer

class LawyersCreate(generics.CreateAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer
class LawyersDelete(generics.DestroyAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer

#################################Reminders API'S#################################
class RemindersList(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class RemindersDetail(generics.RetrieveAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class RemindersUpdateOne(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class RemindersCreate(generics.CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class RemindersDelete(generics.DestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class RemindersToday(generics.ListAPIView):
    serializer_class = TodayReminderSerializer

    def get_queryset(self):
        today = timezone.now().date()
        user = self.request.user.username

        return Reminder.objects.filter(
            datetime__date=today,
            case_id__lawyer__username=user
        ).order_by('datetime')

    #The following function help to overcome the error "case_id:null" for reminders with same case_id
    # def get_serializer_context(self):
    #     # Get the case_id from the queryset
    #     case_id = self.get_queryset().first().case_id_id if self.get_queryset().exists() else None
    #     return {'case_id': case_id}
    
    #The following function help to overcome the error "case_id:null" for reminder of different case_id
    def get_serializer_context(self):
        # Get the queryset of reminders
        queryset = self.get_queryset()

        # Create a dictionary mapping reminder id to its case_id
        reminder_case_ids = {reminder.id: reminder.case_id_id for reminder in queryset}

        # Return the mapping in the serializer context
        return {'reminder_case_ids': reminder_case_ids}
    
class CaseRemindersList(generics.ListAPIView):
    serializer_class = ReminderSerializer

    def get_queryset(self):
        case_id = self.kwargs['pk']
        return Reminder.objects.filter(case_id=case_id)

class CaseRemindersCreate(generics.CreateAPIView):
    serializer_class = ReminderSerializer

    def create(self, request, *args, **kwargs):
        case_id = kwargs.get('pk')
        serializer = self.get_serializer(data=request.data, context={'case_id': case_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


#################################Document API'S#################################
    
class DocumentsList(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class CaseDocumentsList(generics.ListAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        case_id = self.kwargs['pk']
        return Document.objects.filter(case_id=case_id)

class CaseDocumentsCreate(generics.CreateAPIView):
    serializer_class = DocumentSerializer

    def create(self, request, *args, **kwargs):
        case_id = kwargs.get('pk')
        serializer = self.get_serializer(data=request.data, context={'case_id': case_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DocumentsDetail(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentsUpdateOne(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentsCreate(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentsDelete(generics.DestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

#################################Case API'S#################################
    
class CasesList(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class UserCasesList(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def get_queryset(self):
        user = self.request.user
        print(self.request.user)
        return Case.objects.filter(
            lawyer__username=user.username
        )
    
class CasesDetail(generics.RetrieveAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CasesUpdateOne(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CasesCreate(generics.CreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def perform_create(self, serializer):
        # Calling the saved Case and making it as instance 
        case_instance = serializer.save()

        # Get the user id
        user = self.request.user.username

        # Get the Lawyer instance associated with the user
        lawyer_instance = Lawyer.objects.get(username=user)

        # Add the Case instance to the many-to-many relationship
        lawyer_instance.cases.add(case_instance)
        
        lawyer_instance.save()

class CasesDelete(generics.DestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CaseInActive(generics.UpdateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def patch(self, request, pk):
        try:
            case_data = Case.objects.get(pk=pk)
            case_data.case_end_date= timezone.now().date()
            case_data.status = 'I'
            case_data.save()
            serializer = CaseSerializer(case_data, partial=True)
            return JsonResponse({"code": 201, "data": serializer.data})
        except Case.DoesNotExist:
            return JsonResponse({"code": 404, "data": "Case not found"})
        except Exception as e:
            return JsonResponse({"code": 500, "data": str(e)})


class CaseActive(generics.UpdateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def patch(self, request, pk):
        try:
            case_data = Case.objects.get(pk=pk)
            case_data.case_end_date= None
            case_data.status = 'A'
            case_data.save()
            serializer = CaseSerializer(case_data, partial=True)
            return JsonResponse({"code": 201, "data": serializer.data})
        except Case.DoesNotExist:
            return JsonResponse({"code": 404, "data": "Case not found"})
        except Exception as e:
            return JsonResponse({"code": 500, "data": str(e)})


