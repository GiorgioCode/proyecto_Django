# Generated by Django 4.1.7 on 2023-04-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppColegio', '0004_curso_estudiante_alter_entregable_estudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='cursos',
            field=models.ManyToManyField(to='AppColegio.curso'),
        ),
    ]
