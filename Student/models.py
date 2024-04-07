from django.db import models
import os
from django.utils.text import slugify
# Create your models here.

def student_directory_path(instance, filename):
    # Obtain the student's dob and lastname
    dob = instance.student.dob.strftime("%Y-%m-%d")
    lastname = slugify(instance.student.lastname)
    # Build the directory path
    directory_name = f"{dob}-{lastname}"
    # Return the whole path to the file
    return os.path.join('student_attachments', directory_name, filename)



class Student(models.Model):
    email       = models.EmailField(max_length=100)
    firstname   = models.CharField(max_length=255)
    middlename  = models.CharField(max_length=255, null=True, blank=True)
    lastname    = models.CharField(max_length=255)
    photo       = models.ImageField(upload_to='students_photos/', null=True, blank=True)
    address     = models.CharField(max_length=255)
    contact     = models.CharField(max_length=255)
    postcode    = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    dob         = models.DateField()
    religion    = models.CharField(max_length=255, null=True, blank=True)
    gender      = models.CharField(max_length=10)
    disability  = models.TextField(null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)





class Attachment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to=student_directory_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)