# Generated by Django 3.1.5 on 2021-03-10 11:18

from django.db import migrations, models
import django.db.models.deletion
import menu.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloES', models.CharField(max_length=150, verbose_name='Categoría')),
                ('tituloEN', models.CharField(max_length=150, verbose_name='Categoría')),
                ('descripionES', models.CharField(max_length=200, verbose_name='Descripción')),
                ('descripionEN', models.CharField(max_length=200, verbose_name='Descripción')),
                ('icono', models.ImageField(upload_to=menu.models.upload_to_categorias_iconoBlanco, verbose_name='Icono')),                
                ('orden', models.SmallIntegerField(default=0, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'categoría',
                'verbose_name_plural': 'categorías',
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Sugerencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreES', models.CharField(max_length=150, verbose_name='Nombre del plato')),
                ('nombreEN', models.CharField(max_length=150, verbose_name='Nombre del plato')),
                ('descripionES', models.CharField(max_length=200, verbose_name='Descripción')),
                ('descripionEN', models.CharField(max_length=200, verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=menu.models.upload_to_sugerencias, verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'sugerencia del cheff',
                'verbose_name_plural': 'sugerencias del cheff',
                'ordering': ['nombreES'],
            },
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreES', models.CharField(max_length=150, verbose_name='Nombre del plato')),
                ('nombreEN', models.CharField(max_length=150, verbose_name='Nombre del plato')),
                ('descripionES', models.CharField(max_length=200, verbose_name='Descripción')),
                ('descripionEN', models.CharField(max_length=200, verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.categoria')),
            ],
            options={
                'verbose_name': 'plato',
                'verbose_name_plural': 'platos',
                'ordering': ['categoria', 'precio', 'nombreES'],
            },
        ),
    ]