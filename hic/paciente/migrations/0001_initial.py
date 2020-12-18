# Generated by Django 2.2.6 on 2020-12-17 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TAlergia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteAlergia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alergia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paciente.TAlergia')),
                ('historia_clinica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paciente.HistoriaClinica')),
            ],
        ),
    ]
