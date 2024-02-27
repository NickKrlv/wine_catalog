from django.db import models


class Wine(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    grape_variety = models.CharField(max_length=200, verbose_name='Сорт винограда')
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    preview = models.ImageField(upload_to='wines/', verbose_name='Превью', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Наличие')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вино'
        verbose_name_plural = 'Вино'

    def get_absolute_url(self):
        return f'/wines/{self.slug}/'
