from django.urls import path
from .views import HealthcareAIView, index

urlpatterns = [
    path('api/healthcare-ai/', HealthcareAIView.as_view(), name='healthcare_ai'),
    path('', index, name='index'),
]
