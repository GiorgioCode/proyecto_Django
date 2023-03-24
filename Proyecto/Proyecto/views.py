from django.http import HttpResponse
from datetime import datetime


def saluda(request):
    return HttpResponse("Hola a todos desde Django! =)")


def segunda_view(request):
    return HttpResponse("""
            <h1>Bienvenidos a la web de prueba</h1>
            <hr>
            <p> Esto es un parrafo de prueba</p>
                        """)


def dia_hoy(request):
    dia = datetime.now()
    documento = f'Hoy es: <br> {dia}'
    return HttpResponse(documento)
