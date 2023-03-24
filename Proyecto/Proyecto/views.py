from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


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


def saluda_nombre(request, nombre):
    documento = f'Mi nombre es: <br> {nombre}'


def probando_template(request):
    mi_html = open(
        "/Users/jorgeangelpaez/Documents/GitHub/proyecto_Django/Proyecto/Proyecto/templates/primer_template.html")
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)
