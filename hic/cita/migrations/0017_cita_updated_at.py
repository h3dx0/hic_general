# Generated by Django 2.2.6 on 2021-06-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0016_auto_20210504_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]