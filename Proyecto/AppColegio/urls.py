from django.contrib import admin
from django.urls import path
from AppColegio.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<comision>/<codigo>/', curso),
    path('lista_cursos', lista_cursos),
    path('', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]
