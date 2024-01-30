from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    
   #################################Users URLS#################################
    path('auth/register/', views.RegistrationView.as_view()),
    # path('password/verify/', OldPasswordVerificationView.as_view(), name='old-password-verify'),
    path('lawyers/', views.LawyersList.as_view()),
    path('lawyers/create/', views.LawyersCreate.as_view()),
    path('lawyers/<int:pk>/update', views.LawyersUpdateOne.as_view()),
    path('lawyers/<int:pk>/', views.LawyersDetail.as_view()),
    path('lawyers/<int:pk>/delete', views.LawyersDelete.as_view()),

   #################################Reminders URLS#################################

    # path('reminders/', views.Reminders.as_view(), name='reminders_index'),
    path('reminders/', views.RemindersList.as_view()),
    path('reminders/<int:pk>/update', views.RemindersUpdateOne.as_view()),
    path('reminders/<int:pk>/', views.RemindersDetail.as_view()),
    path('reminders/create/', views.RemindersCreate.as_view()),
    path('reminders/<int:pk>/delete', views.RemindersDelete.as_view()),
    path('reminders/today', views.RemindersToday.as_view()),
    path('cases/<int:pk>/reminders/', views.CaseRemindersList.as_view()),
    path('cases/<int:pk>/reminders/create/', views.CaseRemindersCreate.as_view()),    

    #################################Document URLS#################################
    path('documents/', views.DocumentsList.as_view()),
    path('documents/<int:pk>/update', views.DocumentsUpdateOne.as_view()),
    path('documents/<int:pk>/', views.DocumentsDetail.as_view()),
    path('documents/create/', views.DocumentsCreate.as_view()),
    path('documents/<int:pk>/delete', views.DocumentsDelete.as_view()),
    path('cases/<int:pk>/documents/', views.CaseDocumentsList.as_view()),
    path('cases/<int:pk>/documents/create/', views.CaseDocumentsCreate.as_view()),    


    #################################Case URLS#################################
    path('cases/', views.CasesList.as_view()),
    path('usercases/', views.UserCasesList.as_view()),
    path('cases/<int:pk>/update', views.CasesUpdateOne.as_view()),
    path('cases/<int:pk>/', views.CasesDetail.as_view()),
    path('cases/create/', views.CasesCreate.as_view()),
    path('cases/<int:pk>/delete', views.CasesDelete.as_view()),
    path('cases/<int:pk>/caseinactive', views.CaseInActive.as_view()),
    path('cases/<int:pk>/caseactive', views.CaseActive.as_view()),


]