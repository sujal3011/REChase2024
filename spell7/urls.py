from django.urls import path
from . import views

app_name = 'spell7'
urlpatterns = [
    path('', views.home, name='home'),
]
