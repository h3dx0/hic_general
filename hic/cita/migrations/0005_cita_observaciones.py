# Generated by Django 2.2.6 on 2019-10-26 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0004_auto_20191024_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='observaciones',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
