from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet

departmeRouter = DefaultRouter()
departmeRouter.register(r'resource', DepartmentViewSet)


urlpatterns = [
    # path('department', DepartmentViewSet),
    path('', include(departmeRouter.urls)),
    
]
