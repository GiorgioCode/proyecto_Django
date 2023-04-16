from django.shortcuts import render
from .models import Curso, Estudiante, Entregable, Profesor
from django.http import HttpResponse
from .forms import CursoFormulario, EntregableFormulario, EstudianteFormulario, ProfesorFormulario
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


def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso = Curso(
                nombre=data['nombre'], comision=data['comision'], codigo=data['codigo'], imagen=data['imagen'], estudiante=data['estudiante'])
            curso.save()
            lista_cursos = Curso.objects.all()
            return render(request, 'cursos.html', {"cursos": lista_cursos})
        else:
            return HttpResponse('<script>alert("Datos de formulario invalidos")</script>')
    else:
        miFormulario = CursoFormulario()
        return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})


def estudianteFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            print(data)
            estudiante = Estudiante(
                nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            estudiante.save()
            lista_estudiantes = Estudiante.objects.all()
            return render(request, 'estudiantes.html', {"estudiantes": lista_estudiantes})
        else:
            return HttpResponse('<script>alert("Datos de formulario invalidos")</script>')
    else:
        miFormulario = EstudianteFormulario()
        return render(request, "estudianteFormulario.html", {"miFormulario": miFormulario})


def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])
            profesor.save()
            lista_profesores = Profesor.objects.all()
            return render(request, 'profesores.html', {"profesores": lista_profesores})
        else:
            return HttpResponse('<script>alert("Datos de formulario invalidos")</script>')
    else:
        miFormulario = ProfesorFormulario()
        return render(request, "profesorFormulario.html", {"miFormulario": miFormulario})


def entregableFormulario(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            entregable = Entregable(
                nombre=data['nombre'], fecha_entrega=data['fecha_entrega'], entregado=data['entregado'])
            entregable.save()
            lista_entregables = Entregable.objects.all()
            return render(request, 'entregables.html', {"entregables": lista_entregables})
        else:
            return HttpResponse('<script>alert("Datos de formulario invalidos")</script>')
    else:
        miFormulario = EntregableFormulario()
        return render(request, "entregableFormulario.html", {"miFormulario": miFormulario})


def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        curso = Curso.objects.filter(nombre__icontains=nombre)
        print(curso)
        return render(request, 'busquedaComision.html', {"cursos": curso})


def index(request):
    return render(request, 'index.html')


def busquedaComision(request):
    return render(request, 'busquedaComision.html')
