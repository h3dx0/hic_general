# Generated by Django 2.2.6 on 2021-04-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210331_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='InicioFolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.IntegerField(default=0)),
            ],
        ),
    ]
