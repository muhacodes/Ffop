from django.db import models
from account.models import User
from Student.models import  Student
from Lesson.models import Lesson
from Batch.models import  Batch
# Create your models here.


class Invoice(models.Model):
    student         = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson          = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    batch           = models.ForeignKey(Batch, on_delete=models.CASCADE)
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_number  = models.CharField(max_length=255, unique=True)
    comments        = models.CharField(max_length=250, null=True, blank=True)
    discount        = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount          = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid            = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status          = models.CharField(max_length=255, default='Pending')
    invoice_date    = models.DateField(blank=True, null=True)
    due_date        = models.DateField(null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student.lastname} - payment for {self.lesson.name} amount {self.amount}'


class Payment(models.Model):
    invoice         = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount          = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    transaction_id  = models.CharField(max_length=255, null=True, blank=True)
    payment_method  = models.CharField(max_length=255, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.invoice.student.lastname} payment amount {self.amount} on {self.created_at}'