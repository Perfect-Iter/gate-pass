from django.shortcuts import render

from django.http import Http404
from base.models import Device, Student
from base.serializers import StudentSerializer, StudentSerializerDevice

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
        data = request.data 
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDevice(APIView):

    def get(self, request, pk, format=None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializerDevice(student)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializerDevice(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
            

