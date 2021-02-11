# Generated by Django 2.2.6 on 2021-01-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_auto_20201230_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='costo_terapias',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='costo_valoracion',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fecha_cita',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='nombre_entrevistador',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]