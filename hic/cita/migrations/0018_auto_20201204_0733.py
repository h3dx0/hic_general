# Generated by Django 2.2.6 on 2020-12-04 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0017_auto_20201204_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='citas', to='main.Medico'),
        ),
    ]
