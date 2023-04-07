from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    comision = forms.IntegerField(required=True)
    codigo = forms.CharField(required=True)
    imagen = forms.CharField(required=True)


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=False)
    profesion = forms.CharField(max_length=50, required=True)
