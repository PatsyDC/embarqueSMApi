# Generated by Django 4.0 on 2024-07-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_flotadp_cts'),
    ]

    operations = [
        migrations.AddField(
            model_name='flotadp',
            name='essalud',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
