from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ['adm_no','first_name', 'last_name','Major','status']
        fields = '__all__'

class StudentSerializerForm(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['adm_no','first_name', 'last_name','Major','status']
        