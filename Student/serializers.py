from rest_framework import serializers
from django.db.models import Sum
from .models import Student, Attachment
from datetime import date, timedelta
from Batch.serializers import BatchSerializer, Batch
from Invoice.serialiers import  InvoiceSerializer, Invoice


class StudentSerializer(serializers.ModelSerializer):
    batches = serializers.SerializerMethodField()
    invoices = serializers.SerializerMethodField()
    total_amount_paid = serializers.SerializerMethodField()


    class Meta:
        model = Student
        fields = '__all__'

    def get_batches(self, obj):
        print(obj)
        # Assuming Batch has a ManyToManyField to Student without a related_name
        batches = Batch.objects.filter(student=obj.id).first()
        return BatchSerializer(batches).data

    def get_invoices(self, obj):
        # Assuming Invoice has a ForeignKey to Student without a related_name
        invoices = Invoice.objects.filter(student=obj.id)
        return InvoiceSerializer(invoices, many=True).data
    
    def get_total_amount_paid(self, obj):
        # Calculate total amount paid for all batches related to the student
        total_amount_paid = Invoice.objects.filter(student=obj.id).aggregate(total_amount=Sum('paid'))['total_amount']
        return total_amount_paid or 0


    def validate_dob(self, value):
        # Calculate age
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))

        if age < 18:
            raise serializers.ValidationError("Age must be at least 18 years.")
        return value


class StudentAttachmentSerializer(serializers.ModelSerializer):
    file_size = serializers.SerializerMethodField()

    class Meta:
        model = Attachment
        fields = '__all__'

    def get_file_size(self, obj):
        # Ensure there is a file before trying to access its size
        if obj.file and hasattr(obj.file, 'size'):
            return obj.file.size
        return None

    def create(self, validated_data):
        """
        Create and return a new `Attachment` instance, given the validated data.
        """
        return Attachment.objects.create(**validated_data)