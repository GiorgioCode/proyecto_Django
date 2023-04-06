from django.shortcuts import render
from .models import Curso, Estudiante, Entregable, Profesor
from django.http import HttpResponse
# Create your views here.


def inicio(self):
    return render(self, "inicio.html")


def cursos(self):
    lista_cursos = Curso.objects.all()
    return render(self, "cursos.html", {"cursos": lista_cursos})


def profesores(self):
    lista_profesores = Profesor.objects.all()
    return render(self, "profesores.html", {"profesores": lista_profesores})


def estudiante(self):
    lista_estudiantes = Estudiante.objects.all()
    return render(self, "estudiantes.html", {"estudiantes": lista_estudiantes})


def entregables(self):
    lista_entregables = Entregable.objects.all()
    return render(self, "entregables.html", {"entregables": lista_entregables})


def cursoFormulario(request):
    if request.method == 'POST':
        curso = Curso(
            nombre=request.POST['nombre'], comision=request.POST['comision'], codigo=request.POST['codigo'])
        curso.save()
        lista_cursos = Curso.objects.all()
        return render(request, 'cursos.html', {"cursos": lista_cursos})
    return render(request, "cursoFormulario.html")
