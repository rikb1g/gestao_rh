# Generated by Django 5.0.2 on 2024-03-06 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('arquivo', models.FileField(upload_to='documentos')),
                ('pertence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario')),
            ],
        ),
    ]
