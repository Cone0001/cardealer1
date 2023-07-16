from django.urls import path
from .views import initialroom, selectedroom
urlpatterns = [
    path('', initialroom, name='home'),
    path('room/', selectedroom, name='room'),
]