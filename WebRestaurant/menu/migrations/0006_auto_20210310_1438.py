# Generated by Django 3.1.5 on 2021-03-10 13:38

from django.db import migrations, models
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20210310_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='icono',
        ),
        migrations.AddField(
            model_name='categoria',
            name='iconoBlanco',
            field=models.ImageField(default='static/core/images/0103-served-plate_64.png', upload_to=menu.models.upload_to_categorias_iconoBlanco, verbose_name='Icono Blanco'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='iconoNegro',
            field=models.ImageField(default='static/core/images/0103-served-plate_64.png', upload_to=menu.models.upload_to_categorias_iconoNegro, verbose_name='Icono Negro'),
        ),
    ]