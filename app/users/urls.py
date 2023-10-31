from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.my_profile, name='my_profile'),
    path('', include('allauth.urls')),
]
