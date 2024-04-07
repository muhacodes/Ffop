from rest_framework import serializers
from .models import Lesson




class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        # fields = '__all__'
        exclude = ('created_at', 'updated_at',)
        # read_only_fields = ['created_at', 'updated_at']
