# soma_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_index, name='dashboard_index'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('sobre-o-soma/', views.sobre_soma, name='sobre_soma'),
]