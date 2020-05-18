from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец объявления", blank=True,
                               null=True)
    title = models.CharField(max_length=20, verbose_name='Название')
    price = models.IntegerField(default=100, verbose_name='Цена')
    content = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    # salons = models.ManyToManyField(Salon, verbose_name='Салон')
    # photos = models.ManyToManyField(CarImage, verbose_name='Изображение')

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Car, on_delete=models.CASCADE,verbose_name='Автообъявление', blank=True, null=True,
                                related_name = 'comments_cars')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Тект комментария')
    status = models.BooleanField(verbose_name='Видимость комментария', default=False)