# Generated by Django 4.0 on 2024-08-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_alter_diariodepesca_zona_pesca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diariodepesca',
            name='porcentaje',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
