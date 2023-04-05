from django.contrib import admin
from django.urls import path
from AppColegio.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<comision>/<codigo>/', curso),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
]
