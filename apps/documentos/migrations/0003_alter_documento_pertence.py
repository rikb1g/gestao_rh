# Generated by Django 5.0 on 2023-12-28 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_rename_nome_documento_descricao_documento_pertence'),
        ('funcionarios', '0002_funcionario_departamentos_funcionario_empresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]
