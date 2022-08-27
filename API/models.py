from taggit.managers import TaggableManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', blank=True)
    text = models.TextField(verbose_name='Текст', blank=True)
    link = models.URLField(verbose_name='Ссылка на новость', unique=True)
    date = models.CharField(verbose_name='Дата выгрузки новости', blank=True, max_length=100)
    # taggs = TaggableManager()
    taggs = models.CharField(verbose_name='Теги', max_length=100, default='max')

    class Meta:
        def __str__(self):
            return News.title

        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'






