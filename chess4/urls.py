from django.urls import path
from . import views

app_name = 'chess4'
urlpatterns = [
    path('', views.home, name='home'),
]
