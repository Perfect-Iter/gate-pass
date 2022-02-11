from django.urls import path

from base.views import StudentList

urlpatterns = [

    
    path('students/', StudentList.as_view(), name='students'),


]