from django import forms


class CursoFormulario(forms.Form):
    curso = forms.CharField(required=True)
    comision = forms.IntegerField(required=True)
    codigo = forms.CharField(required=True)
