from django.db.models import Count, Sum, F
from django.db.models import Q
from django.db.models.functions import Coalesce
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

from account.models import User
from Department.models import Department
from Batch.models import Batch
from Lesson.models import Lesson
from Student.models import Student
from account.serializers import UserSerializer

class Home(APIView):
    def get(self, request, format=None):
        data = {}

        # Number of Lessons
        data['total_lessons'] = Lesson.objects.count()

        # Number of Batches
        data['total_batches'] = Batch.objects.count()

        data['total_students'] = Student.objects.count()

        users = User.objects.all() 
        data['total_users'] = UserSerializer(users, many=True).data

        # Potential Revenue (assuming price * students count per batch)
        # data['potential_revenue'] = Batch.objects.annotate(
        #     total_students=Coalesce(Sum('student__count'), 0),
        #     revenue=F('price') * F('total_students')
        # ).aggregate(Sum('revenue'))['revenue__sum'] or 0

        # Batches per Department
        departments_batches = Department.objects.annotate(
        batches_count=Count('batches', filter=Q(batches__isnull=False))
        ).values('name', 'batches_count').distinct()
        data['departments_batches'] = departments_batches

        # Upcoming Batches
        upcoming_batches = Batch.objects.filter(
            start_date__gt=timezone.now()
        ).annotate(totalStudents=Count('student')).values('name', 'totalStudents', 'start_date', 'department__name', 'id', 'lesson__name', 'end_date') # Limit to 10 for example
        data['upcoming_batches'] = list(upcoming_batches)

        total_revenue = Batch.objects.annotate(
            total_amount=F('price') * Count('student')
        ).aggregate(
            total_revenue=Sum('total_amount')
        )['total_revenue']
        data['total_revenue'] = total_revenue

        return Response(data)
