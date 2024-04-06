from django.urls import path
from . import views

app_name = 'turbanNumbers'
urlpatterns = [
    path('', views.home, name='home'),
]
