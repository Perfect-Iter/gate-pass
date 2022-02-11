from django.shortcuts import render

from django.http import Http404
from base.models import Student
from base.serializers import StudentSerializer, StudentSerializerForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class StudentList(APIView):

    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = StudentSerializerForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
