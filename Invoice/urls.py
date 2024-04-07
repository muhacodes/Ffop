from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, PaymentViewSet

InvoiceRouter = DefaultRouter()
InvoiceRouter.register(r'resource', InvoiceViewSet)

PaymentRouter = DefaultRouter()
PaymentRouter.register(r'payment/resource', PaymentViewSet)


urlpatterns = [
    # path('department', DepartmentViewSet),
    path('', include(PaymentRouter.urls)),

    
]
