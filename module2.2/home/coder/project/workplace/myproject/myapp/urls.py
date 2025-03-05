from django.urls import path
from .views import drinks

urlpatterns = [
    path('drinks/<str:drink_name>/', drinks, name='drinks'),
]
