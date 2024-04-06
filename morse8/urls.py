from django.urls import path
from . import views

app_name = 'morse8'
urlpatterns = [
    path('', views.home, name='home'),
]
