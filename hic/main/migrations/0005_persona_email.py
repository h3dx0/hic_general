# Generated by Django 2.2.6 on 2019-11-01 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191028_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='email',
            field=models.CharField(default='a', max_length=80, unique=True),
            preserve_default=False,
        ),
    ]