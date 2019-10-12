# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-12 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='medico_especialidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.EspecialidadMedico'),
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Paciente'),
        ),
        migrations.AddField(
            model_name='cita',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cita.TCita'),
        ),
        migrations.AddField(
            model_name='calendario',
            name='medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Medico'),
        ),
    ]
