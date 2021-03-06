# Generated by Django 2.2.6 on 2021-02-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0008_auto_20210211_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='escolaridad_menor',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='estado_civil',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='folio',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='grado_cursa',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='nombre_colegio',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='nombre_madre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='nombre_padre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='ocupacion_madre',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='ocupacion_padre',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='remitido_por',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='servicio_solicitado',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='telefono_madre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='telefono_padre',
            field=models.CharField(max_length=150),
        ),
    ]
