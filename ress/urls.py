from django.urls import path
from ress import views

urlpatterns = [
    path('', views.home, name='home'),
]
