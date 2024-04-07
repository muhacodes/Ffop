from django.db import models

from Department.models import Department
# Create your models here.
class Lesson(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)