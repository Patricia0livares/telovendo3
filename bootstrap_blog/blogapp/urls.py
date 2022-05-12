from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('proveedor/', views.ingresoproveedor, name='proveedor'),
]