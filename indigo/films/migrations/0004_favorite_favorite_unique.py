# Generated by Django 3.2.3 on 2024-12-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_favorite'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('film', 'user'), name='favorite_unique'),
        ),
    ]
