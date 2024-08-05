# Generated by Django 4.0 on 2024-08-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_flotadp_precio_bereche_flotadp_precio_merluza_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flotadp',
            name='costo_agua',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flotadp',
            name='costo_gasolina',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flotadp',
            name='costo_hilo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
