from django.db import models
from Department.models import Department
from Lesson.models import Lesson
from Student.models import Student
# Create your models here.


class Batch(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='batches')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='batches')
    student = models.ManyToManyField(Student,null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)