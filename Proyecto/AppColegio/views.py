from django.shortcuts import render
from .models import Curso, Estudiante, Entregable, Profesor
from django.http import HttpResponse
from .forms import CursoFormulario
from django.db.models import Q
from datetime import datetime
# Create your views here.


def inicio(self):
    lista_cursos = Curso.objects.all()
    return render(self, "inicio.html", {"cursos": lista_cursos})


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


# version formulario html
""" def cursoFormulario(request):
    if request.method == 'POST':
        curso = Curso(
            nombre=request.POST['nombre'], comision=request.POST['comision'], codigo=request.POST['codigo'])
        curso.save()
        lista_cursos = Curso.objects.all()
        return render(request, 'cursos.html', {"cursos": lista_cursos})
    return render(request, "cursoFormulario.html") """


def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso = Curso(
                nombre=data['nombre'], comision=data['comision'], codigo=data['codigo'], imagen=data['imagen'])
            curso.save()
            lista_cursos = Curso.objects.all()
            return render(request, 'cursos.html', {"cursos": lista_cursos})
        else:
            return HttpResponse('<script>alert("Datos de formulario invalidos")</script>')
    else:
        miFormulario = CursoFormulario()
        return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})


def busquedaComision(request):
    return render(request, 'busquedaComision.html')


def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        curso = Curso.objects.filter(nombre__icontains=nombre)
        print(curso)
        return render(request, 'busquedaComision.html', {"cursos": curso})


def index(request):
    return render(request, 'index.html')
