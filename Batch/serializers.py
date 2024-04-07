from rest_framework import serializers
from .models import Batch, Department, Lesson

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['id', 'department', 'lesson', 'name',  'price', 'start_date', 'end_date', 'created_at', 'updated_at']
        read_only_fields = ['name']

    # Optionally, specify more detailed field types or validation here
    # For example, to display dropdowns with object representations:
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all())
