# Generated by Django 5.0.6 on 2024-06-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0004_remove_clients_nombre_clients_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='telephone',
            field=models.CharField(max_length=9, verbose_name='Número de Teléfono'),
        ),
    ]
