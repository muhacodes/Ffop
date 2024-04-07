from django.shortcuts import render
from rest_framework import viewsets, status
from .models import  Student,  Attachment
from .serializers import StudentSerializer, StudentAttachmentSerializer
from rest_framework.response import Response

# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class StudentAttachmentViewset(viewsets.ModelViewSet):
    serializer_class = StudentAttachmentSerializer

    def get_queryset(self):
        """
        Filter the attachments by a 'student' query parameter. 
        Returns an empty queryset if 'student' is not provided.
        """
        student_id = self.request.query_params.get('student', None)
        if student_id is not None:
            return Attachment.objects.filter(student__id=student_id)
        else:
            # Option 1: Return an empty queryset
            return Attachment.objects.none()

    def create(self, request, *args, **kwargs):
        """
        Handle file upload.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the attachment
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)