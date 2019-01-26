# Generated by Django 2.1.5 on 2019-01-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('numero_guia_consulta', models.IntegerField(primary_key=True, serialize=False)),
                ('cod_medico', models.IntegerField()),
                ('nome_medico', models.CharField(blank=True, max_length=5000, null=True)),
                ('data_consulta', models.DateField(blank=True, null=True)),
                ('valor_consulta', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'consulta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('cod_exame', models.IntegerField(primary_key=True, serialize=False)),
                ('valor_exame', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'exame',
                'managed': False,
            },
        ),
    ]
