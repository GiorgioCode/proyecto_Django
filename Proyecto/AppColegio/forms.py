from django import forms
from .models import Entregable, Estudiante, Curso, Profesor
from django.forms import ModelForm


class CursoFormulario(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'comision', 'codigo', 'imagen']


class ProfesorFormulario(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion', 'cursos']


class EntregableFormulario(ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_entrega', 'entregado', 'estudiante']


class EstudianteFormulario(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'cursos']
