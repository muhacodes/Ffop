from django.shortcuts import render, get_object_or_404
from .serialiers import InvoiceSerializer, PaymentSerializer
from rest_framework import viewsets, status
from .models import Invoice, Payment
from rest_framework.response import Response
from Student.models import Student
from django.db.models import Sum
# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer



class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # student = Student.objects.get(id=request.data.get('student'))
        student = get_object_or_404(Student,id=request.data.get('student'))

        invoice = student.invoice_set.all().first()
        if not invoice:
            return Response({'error': 'Invoice not found for the student'}, status=status.HTTP_404_NOT_FOUND)
        

        serializer.validated_data['invoice'] = invoice

        
        payment_amount = serializer.validated_data.get('amount')

        # Optionally, check if the new payment exceeds the amount due
        total_paid_already = invoice.payment_set.aggregate(Sum('amount'))['amount__sum'] or 0
        new_total = total_paid_already + payment_amount
        if new_total > invoice.amount:
            return Response({'error': 'Payment exceeds the amount due'}, status=status.HTTP_400_BAD_REQUEST)
        
        payment = serializer.save()
        invoice.paid = new_total
        
        # Update the invoice status based on the new total paid
        if invoice.paid >= invoice.amount:
            invoice.status = 'Paid'
        else:
            invoice.status = 'Partially Paid'
        
        invoice.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)