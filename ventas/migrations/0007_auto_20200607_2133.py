# Generated by Django 3.0.6 on 2020-06-08 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_imagenproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproducto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
