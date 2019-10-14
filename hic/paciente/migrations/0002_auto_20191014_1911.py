# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-14 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antecedente',
            name='historia_clinica',
        ),
        migrations.RemoveField(
            model_name='santecedente',
            name='medico',
        ),
        migrations.RemoveField(
            model_name='santecedentetalergia',
            name='s_antecedente',
        ),
        migrations.RemoveField(
            model_name='santecedentetalergia',
            name='t_alergia',
        ),
        migrations.RemoveField(
            model_name='antecedentealergia',
            name='antecedente',
        ),
        migrations.AddField(
            model_name='antecedentealergia',
            name='historia_clinica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paciente.HistoriaClinica'),
        ),
        migrations.DeleteModel(
            name='Antecedente',
        ),
        migrations.DeleteModel(
            name='SAntecedente',
        ),
        migrations.DeleteModel(
            name='SAntecedenteTAlergia',
        ),
    ]
