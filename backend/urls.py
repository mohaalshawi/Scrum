from django.urls import path
from . import views as user_views

urlpatterns = [
    path('login/', user_views.user_login, name='login'),
    path('register/', user_views.user_register, name='register'),
]