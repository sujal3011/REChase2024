from django.urls import path
from . import views

app_name = 'coordinates'
urlpatterns = [
    path('', views.home, name='home'),
]
