# Generated by Django 4.0 on 2024-08-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_diariodepesca_p_flota_dolares_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diariodepesca',
            name='numero',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
