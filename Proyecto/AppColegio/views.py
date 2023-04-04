from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.


def curso(self, nombre, comision, codigo):
    curso = Curso(nombre=nombre, comision=comision, codigo=codigo)
    curso.save()

    return HttpResponse(f"""
                        <h2> Curso: {curso.nombre}</h2>
                        <hr>
                        <h3> Comision: {curso.comision}</h2>
                        <h3> Codigo: {curso.codigo}</h2>
                        """)


def lista_cursos(self):
    lista = Curso.objects.all()
    return render(self, "lista_cursos.html", {"lista_cursos": lista})
