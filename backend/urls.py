from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    # Include other paths here
]