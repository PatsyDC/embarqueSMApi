# Generated by Django 4.0 on 2024-07-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_flotadp_total_participacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flotadp',
            name='total_participacion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
