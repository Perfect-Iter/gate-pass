from django.urls import path

from base.views import StudentDevice, StudentList

urlpatterns = [

    
    path('students/', StudentList.as_view(), name='students'),
    path("students/<str:pk>/", StudentDevice.as_view(), name="student-device"),


]