from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, deletar


urlpatterns = [
    path('', home),
    path('salvar/', salvar, name='salvar'), 
    path('editar/<int:pessoa_id>/', editar, name='editar'),
    path('deletar/<int:pessoa_id>/', deletar, name='deletar'),
]