from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('contract/', views.contract, name='contract'),
]
