# Generated by Django 3.2.7 on 2021-10-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamientos', '0004_auto_20211026_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alojamiento',
            name='abrir',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='alojamiento',
            name='cerrar',
            field=models.TimeField(null=True),
        ),
    ]
