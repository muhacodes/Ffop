from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  LessonnViewSet

lessonmeRouter = DefaultRouter()
lessonmeRouter.register(r'resource', LessonnViewSet)


urlpatterns = [
    # path('department', DepartmentViewSet),
    path('', include(lessonmeRouter.urls)),
    
]
