# Generated by Django 4.1.7 on 2023-04-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppColegio', '0002_remove_curso_estudiante_remove_entregable_estudiante_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='estudiante',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='cursos',
            field=models.ManyToManyField(to='AppColegio.curso'),
        ),
    ]