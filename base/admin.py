from distutils.command.check import check
from django.contrib import admin

from .models import Checkin, Device, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Device)
admin.site.register(Checkin)