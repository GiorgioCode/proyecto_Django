from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Estudiante, Entregable, Profesor
from django.http import HttpResponse
from .forms import CursoFormulario, EntregableFormulario, EstudianteFormulario, ProfesorFormulario
from django.db.models import Q
from datetime import datetime
# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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
            miFormulario = CursoFormulario()
            return render(request, "cursoFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
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
            miFormulario = EstudianteFormulario()
            return render(request, "estudianteFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = EstudianteFormulario()
        return render(request, "estudianteFormulario.html", {"miFormulario": miFormulario})


def eliminarEstudiante(request, id):
    if request.method == 'POST':
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        lista_profesores = Profesor.objects.all()
        return render(request, 'profesores.html', {"profesores": lista_profesores})


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
            miFormulario = ProfesorFormulario()
            return render(request, "profesorFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = ProfesorFormulario()
        return render(request, "profesorFormulario.html", {"miFormulario": miFormulario})


def eliminarProfesor(request, id):
    if request.method == 'POST':
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        lista_profesores = Profesor.objects.all()
        return render(request, 'profesores.html', {"profesores": lista_profesores})


def editarProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor.nombre = data['nombre']
            profesor.email = data['email']
            profesor.apellido = data['apellido']
            profesor.profesion = data['profesion']
            profesor.save()
            lista_profesores = Profesor.objects.all()
            return render(request, 'profesores.html', {"profesores": lista_profesores})
        else:
            miFormulario = ProfesorFormulario()
            return render(request, "profesorFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "email": profesor.email,
            "apellido": profesor.apellido,
            "profesion": profesor.profesion,
        })
        return render(request, "editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})


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
            miFormulario = EntregableFormulario()
            return render(request, "entregableFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = EntregableFormulario()
        return render(request, "entregableFormulario.html", {"miFormulario": miFormulario})


def eliminarEntregable(request, id):
    if request.method == 'POST':
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        lista_profesores = Profesor.objects.all()
        return render(request, 'profesores.html', {"profesores": lista_profesores})


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


class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'listaCursos.html'
    context_object_name = 'cursos'


class CursoDetail(DetailView):
    model = Curso
    template_name = 'detalleCurso.html'
    context_object_name = 'curso'


class CursoUpdate(UpdateView):
    model = Curso
    template_name = 'editarCurso.html'
    fields = ['nombre', 'comision', 'codigo', 'imagen']
    success_url = '/listaCursos/'


class CursoDelete(DeleteView):
    model = Curso
    template_name = 'eliminarCurso.html'
    success_url = '/app-colegio/listaCursos/'
    context_object_name = 'curso'


class CursoCreate(CreateView):
    model = Curso
    template_name = 'crearCurso.html'
    fields = ['nombre', 'comision', 'codigo', 'imagen']
    success_url = '/listaEntregables/'


class EntregableList(ListView):
    model = Entregable
    template_name = 'listaEntregables.html'
    context_object_name = 'entregables'


class EntregableDetail(DetailView):
    model = Entregable
    template_name = 'detalleEntregable.html'
    context_object_name = 'entregable'


class EntregableUpdate(UpdateView):
    model = Entregable
    template_name = 'editarEntregable.html'
    fields = ['nombre', 'fecha_entrega', 'entregado']
    success_url = '/listaEntregables/'


class EntregableDelete(DeleteView):
    model = Entregable
    template_name = 'eliminarEntregable.html'
    success_url = '/app-colegio/listaEntregables/'
    context_object_name = 'entregable'


class EntregableCreate(CreateView):
    model = Entregable
    template_name = 'crearEntregable.html'
    fields = ['nombre', 'fecha_entrega', 'entregado']
    success_url = '/app-colegio/listaEntregables/'


def user_login(request):
    if request.method == 'POST':
        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data['username']
            password = data['password']
            user = authenticate(username=usuario, password=password)
            if user:
                login(request, user)
                return render(request, "inicio.html")
            else:
                miFormulario = AuthenticationForm()
                return render(request, 'userLogin.html', {'miFormulario': miFormulario, 'error': 'credenciales de usuario incorrectas'})
        else:
            miFormulario = AuthenticationForm()
            return render(request, 'userLogin.html', {'miFormulario': miFormulario, 'error': 'Ha ocurrido un error, por favor intentalo de nuevo'})
    else:
        miFormulario = AuthenticationForm()
        return render(request, 'userLogin.html', {'miFormulario': miFormulario})


def user_signup(request):
    if request.method == 'GET':
        return render(request, 'userSignup.html', {'miFormulario': UserCreationForm, 'estado': ""})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('Inicio')
            except IntegrityError:
                return render(request, 'userSignup.html', {'miFormulario': UserCreationForm, 'error1': True})
        else:
            return render(request, 'userSignup.html', {'miFormulario': UserCreationForm, 'error2': True})


def user_logout(request):
    logout(request)
    return redirect('Inicio')
