from django.db import models


class Articles(models.Model):
    """
    Статьи
    """
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    user_id = models.IntegerField(verbose_name='user_id')
    status = models.TextField(verbose_name='Статус')
    keywords = models.TextField(verbose_name='Ключевые слова')
    structure = models.TextField(verbose_name='Содержание', default='[]')
    content = models.TextField(verbose_name='Контент', default='{}')

    def __str__(self):
        return str(self.id)


class Config(models.Model):
    """
    Промты и т. д.
    """
    class Meta:
        verbose_name = 'Конфигурация'
        verbose_name_plural = 'Конфигурация'

    promt_items = models.TextField(verbose_name='Промт для получения списка статей')
    promt_article = models.TextField(verbose_name='Промт для получения текста')