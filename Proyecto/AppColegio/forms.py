from django import forms
from .models import Entregable, Estudiante, Curso, Profesor
from django.forms import ModelForm


class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    comision = forms.IntegerField(required=True)
    codigo = forms.CharField(required=True)
    imagen = forms.CharField(required=True)


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    profesion = forms.CharField(max_length=50)


class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField(required=False)


class EstudianteFormulario(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']
