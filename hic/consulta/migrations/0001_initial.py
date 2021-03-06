# Generated by Django 2.2.6 on 2020-12-17 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('historia_clinica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paciente.HistoriaClinica')),
                ('medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='NotaPadecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consulta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consulta.Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='SConsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='SNotaPadecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=False)),
                ('s_consulta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consulta.SConsulta')),
            ],
        ),
        migrations.CreateModel(
            name='TConsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TSignoVital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SNotaPadecimientoTSignoVital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=False)),
                ('s_nota_padecimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consulta.SNotaPadecimiento')),
                ('t_signo_vital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consulta.TSignoVital')),
            ],
        ),
        migrations.CreateModel(
            name='SignoVital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consulta.TSignoVital')),
            ],
        ),
        migrations.CreateModel(
            name='NotaPadecimientoSignoVital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_padecimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consulta.NotaPadecimiento')),
                ('signo_vital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consulta.SignoVital')),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consulta.TConsulta'),
        ),
    ]
