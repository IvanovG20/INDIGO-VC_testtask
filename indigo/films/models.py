from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


LENGHT_CONST = 100


class Film(models.Model):
    """Модель фильма"""

    post_author = models.ForeignKey(
        User,
        verbose_name='Автор поста',
        related_name='film_author',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Название фильма',
        max_length=LENGHT_CONST,
    )
    director = models.CharField(
        'Режиссёр фильма',
        max_length=LENGHT_CONST,
    )
    description = models.TextField(
        'Описание фильма',
        null=True,
        blank=True
    )
    release_date = models.DateField(
        'Дата выпуска фильма'
    )
    image = models.ImageField(
        'Постер фильма',
        upload_to='films/',
        null=True,
        blank=True,
    )

    favorited = models.ManyToManyField(
        User,
        through='Favorite',
        related_name='fav_film'
    )

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.name


class Favorite(models.Model):
    """Модель избранного"""

    film = models.ForeignKey(
        Film,
        verbose_name='Фильм',
        related_name='favorite',
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='favorite',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('film', 'user'),
                name='favorite_unique'
            )
        ]

        verbose_name = 'избранное'
        verbose_name_plural = 'избранное'
