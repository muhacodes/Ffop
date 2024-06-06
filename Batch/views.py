from rest_framework import viewsets, status
from .models import Batch
from .serializers import BatchSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
import datetime
from Department.models import  Department
from Lesson.models import Lesson
from Student.models import Student
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from django.shortcuts import HttpResponse
from Student.serializers import StudentSerializer
from Invoice.models import Invoice
from account.models import User




# Create your views here.
class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [AllowAny,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # # Extracting IDs from the department and lesson instances
        department_Initial = serializer.validated_data['department'].name[:1]
        lesson_Initial = serializer.validated_data['lesson'].name[:3]


        start_day = datetime.datetime.strftime(serializer.validated_data['start_date'], "%d-%m/")
        end_day = datetime.datetime.strftime(serializer.validated_data['end_date'], "%d-%m/%Y")

        batchId = f"{department_Initial}{lesson_Initial}{start_day}{end_day}"

        serializer.validated_data['name'] = batchId

        batch = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @action(detail=True, methods=['post'], url_path='add-student')
    def add_student(self, request, pk=None):
        batch = self.get_object()
        student_id = request.data.get('student_id')

        if not student_id:
            return Response({'message': 'Student ID not found.. !'}, status=status.HTTP_404_NOT_FOUND)

        try:
            student = Student.objects.get(id=student_id)
            batch.student.add(student)

            # batchInstance = Batch.objects.get(id=batch)

            invoice = Invoice.objects.create(
                student=student,
                batch=batch,
                lesson=batch.lesson,
                amount=batch.lesson.price,
                invoice_number= f'{student.firstname}-{student.dob}-{batch.end_date}',
                created_by= request.user
            )
            
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Student added to batch successfully'}, status=status.HTTP_200_OK)

    
    @action(detail=True, methods=['get'], url_path='students')
    def get_students(self, request, pk=None):
        try:
            batch = self.get_object()
            students = batch.student.all()  # Assuming 'student' is the related_name in the Batch model's M2M field
            serializer = StudentSerializer(students, many=True, context={'request': request})
            return Response(serializer.data)
        except Batch.DoesNotExist:
            return Response({'message': 'Batch not found'}, status=status.HTTP_404_NOT_FOUND)
            
    
    @action(detail=True, methods=['post'], url_path='remove-student')
    def remove_student(self, request, pk=None):
        batch = self.get_object()  # Get the batch instance for the given pk
        student_id = request.data.get('student_id')  # Get the student_id from the request data

        if not student_id:
            return Response({'message': 'Student ID not found.. !'}, status=status.HTTP_404_NOT_FOUND)
        
        # Try to remove the student from the batch
        try:
            student = Student.objects.get(id=student_id)  # Find the student by ID
            batch.student.remove(student)  # Remove the student from the batch
            invoice = Invoice.objects.get(student=student)
            invoice.delete()
            
            return Response({'message': 'Student removed from batch successfully'}, status=status.HTTP_200_OK)

        except Invoice.DoesNotExist:
            return Response({'message': 'Failed to Delete invoice'}, status=status.HTTP_404_NOT_FOUND)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)