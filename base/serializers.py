from rest_framework import serializers
from .models import Checkin, Device, Student


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['serial_no', 'type', 'model']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['adm_no','first_name', 'last_name','Major','status']




class StudentSerializerDevice(serializers.ModelSerializer):
    devices = DeviceSerializer(read_only=True, many=True)
    class Meta:
        model = Student
        fields = ['adm_no','first_name', 'last_name','Major','status', 'devices']
        #depth = 1


class checkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = ['adm_no', 'serial_no']        