# Generated by Django 2.2.6 on 2020-12-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='direccion',
            field=models.TextField(blank=True, null=True),
        ),
    ]