# Generated by Django 3.2.7 on 2021-10-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_articulo_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre Completo')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('phone', models.IntegerField(max_length=10, verbose_name='Número de Teléfono')),
                ('rfc', models.CharField(max_length=14, verbose_name='RFC')),
                ('email', models.CharField(max_length=50, verbose_name='E-MAIL')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre Completo')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('phone', models.IntegerField(max_length=10, verbose_name='Número de Teléfono')),
                ('email', models.CharField(max_length=50, verbose_name='E-MAIL')),
                ('numdocumento', models.IntegerField(max_length=6, verbose_name='Número de Documento')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre Completo')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('phone', models.IntegerField(max_length=10, verbose_name='Número de Teléfono')),
                ('curp', models.CharField(max_length=20, verbose_name='CURP')),
                ('nss', models.CharField(max_length=10, verbose_name='Número de Seguro Social')),
                ('rfc', models.CharField(max_length=14, verbose_name='RFC')),
                ('email', models.CharField(max_length=50, verbose_name='E-MAIL')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]