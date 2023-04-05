from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nombre} - {self.comision}'
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, null="Desconocido")


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, null="Desconocido")

    def __str__(self):
        return f'{self.nombre} - {self.fecha_entrega}'
