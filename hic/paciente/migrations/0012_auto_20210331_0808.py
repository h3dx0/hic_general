# Generated by Django 2.2.6 on 2021-03-31 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0011_auto_20210225_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='folio',
            field=models.IntegerField(),
        ),
    ]