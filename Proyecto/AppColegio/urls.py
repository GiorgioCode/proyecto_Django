from django.contrib import admin
from django.urls import path
from AppColegio.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiante, name="Estudiantes"),
    path('cursoformulario/', cursoFormulario, name="CursoFormulario"),
    path('listaCursos/', CursoList.as_view(), name="ListaCursos"),
    path('detalleCurso/<pk>/', CursoDetail.as_view(), name="DetalleCurso"),
    path('editarCurso/<pk>/', CursoUpdate.as_view(), name="EditarCurso"),
    path('crearCurso/', CursoCreate.as_view(), name="CrearCurso"),
    path('eliminarCurso/<pk>/', CursoDelete.as_view(), name="EliminarCurso"),
    path('listaEntregables/', EntregableList.as_view(), name="ListaEntregables"),
    path('detalleEntregable/<pk>/',
         EntregableDetail.as_view(), name="DetalleEntregable"),
    path('editarEntregable/<pk>/',
         EntregableUpdate.as_view(), name="EditarEntregable"),
    path('crearEntregable/', EntregableCreate.as_view(), name="CrearEntregable"),
    path('eliminarEntregable/<pk>/',
         EntregableDelete.as_view(), name="EliminarEntregable"),
    path('profesorformulario/', profesorFormulario, name="ProfesorFormulario"),
    path('eliminarprofesor/<int:id>', eliminarProfesor, name='EliminarProfesor'),
    path('editarprofesor/<int:id>', editarProfesor, name='EditarProfesor'),
    path('estudianteformulario/', estudianteFormulario,
         name="EstudianteFormulario"),
    path('eliminarestudiante/<int:id>',
         eliminarEstudiante, name='EliminarEstudiante'),
    path('entregableformulario/', entregableFormulario,
         name="EntregableFormulario"),
    path("busquedaComision", busquedaComision, name="BusquedaComision"),
    path('buscar/', buscar, name="Buscar"),
    path('login/', user_login, name="Login"),
    path('signup/', user_signup, name="Signup"),
    path('logout/', user_logout, name="Logout")
]
