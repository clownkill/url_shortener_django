from django.db import models
from django.core import validators


class Url(models.Model):
    slug = models.SlugField(
        max_length=6,
        primary_key=True,
        verbose_name='Сокращенная ссылка'
    )
    full_url = models.URLField(
        max_length=200,
        verbose_name='Полная ссылка',
        validators=[validators.URLValidator,]
    )
    creation_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата создания ссылки'
    )
    count_clicks = models.IntegerField(
        default=0,
        verbose_name='Количество переходов по ссылке'
    )

    def __str__(self):
        return self.full_url

    class Meta:
        verbose_name_plural = 'Ссылки'
        verbose_name = 'Ссылка'
        ordering = ('-creation_date',)
