# Generated by Django 2.2.6 on 2021-02-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0010_auto_20210211_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='costo_valoracion',
            field=models.CharField(blank=True, default=0, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='escolaridad_menor',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='nombre_madre',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='nombre_padre',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='profesional_cargo',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='remitido_por',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='servicio_solicitado',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='telefono_madre',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='telefono_padre',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]