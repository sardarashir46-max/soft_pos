
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('starter/', views.starter_page, name='starter_page'),
]
