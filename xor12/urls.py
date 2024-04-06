from django.urls import path
from . import views

app_name = 'xor12'
urlpatterns = [
    path('', views.home, name='home'),
]
