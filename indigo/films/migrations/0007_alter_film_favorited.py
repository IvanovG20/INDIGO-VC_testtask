# Generated by Django 3.2.3 on 2024-12-06 12:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0006_auto_20241206_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='favorited',
            field=models.ManyToManyField(related_name='fav_film', through='films.Favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
