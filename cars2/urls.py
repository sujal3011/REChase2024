from django.urls import path
from . import views

app_name = 'cars2'
urlpatterns = [
    path('', views.home, name='home'),
]
