
from django.urls import path
from .import views


urlpatterns = [
    path('', views.authorization, name='home'),
    path('registration/', views.registration, name='registration'),
    path('register/', views.register, name='register'),
    path('main/', views.main, name='main'),
]