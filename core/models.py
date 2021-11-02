from django.db import models


class Service(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    photo = models.ImageField(verbose_name='Фото', upload_to='service/')
    description = models.TextField(verbose_name='Описание')
    phone = models.CharField(verbose_name='Телефон', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
