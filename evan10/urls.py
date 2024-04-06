from django.urls import path
from . import views

app_name = 'evan10'
urlpatterns = [
    path('', views.home, name='home'),
]
