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

# from rest_framework import permissions
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

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
    serializer_class = ReminderSerializer

    def get_queryset(self):
        today = timezone.now().date()
        return Reminder.objects.filter(date__date=today)

#################################Document API'S#################################
    
class DocumentsList(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

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

class CasesDetail(generics.RetrieveAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CasesUpdateOne(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CasesCreate(generics.CreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

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













#################################First Approach#################################    
# class Reminders(APIView):
#     def get(self, request):
#         reminders = Reminder.objects.all()
#         serialized_reminders = ReminderSerializer(reminders, many=True).data
#         return Response(serialized_reminders)

#     def post(self, request):
#         serializer = ReminderSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

# @api_view(['GET'])
#@permission_classes([IsAuthenticated])
# def reminders_index(request):
#     # reminders = Reminder.objects.filter()
#     reminders = Reminder.objects.all()
#     serializer = ReminderSerializer(reminders, many=True)
#     return JsonResponse(serializer.data, safe=False)
