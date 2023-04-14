from django.contrib import admin
from django.urls import path
from AppColegio.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiante, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('cursoformulario/', cursoFormulario, name="CursoFormulario"),
    path('profesorformulario/', profesorFormulario, name="ProfesorFormulario"),
    path('estudianteformulario/', estudianteFormulario,
         name="EstudianteFormulario"),
    path('entregableformulario/', entregableFormulario,
         name="EntregableFormulario"),
    path("busquedaComision", busquedaComision, name="BusquedaComision"),
    path('buscar/', buscar, name="Buscar"),
]
