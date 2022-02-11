from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('signed-in', 'signed-in'),
    ('signed-out', 'signed-out'),
    ('passive', 'passive'),
)


class Student(models.Model):
    adm_no = models.CharField(max_length=10,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Major = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    updated_at =   models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adm_no

class Device(models.Model):
    serial_no = models.CharField(max_length=12)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)
    updated_at =   models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adm_no

class Checkin(models.Model):
    adm_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    serial_no = models.ForeignKey(Device, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adm_no
    
    class Meta:
        ordering = ['-created_at']