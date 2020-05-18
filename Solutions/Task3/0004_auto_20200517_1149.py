# Generated by Django 3.0.6 on 2020-05-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0003_auto_20200517_0255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='carimage',
            options={'verbose_name': 'картинка автомобиля', 'verbose_name_plural': 'Картинки автомобилей'},
        ),
        migrations.AlterModelOptions(
            name='salon',
            options={'verbose_name': 'адрес автосалона', 'verbose_name_plural': 'Адреса автосалонов'},
        ),
        migrations.RemoveField(
            model_name='car',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='car',
            name='salons',
        ),
        migrations.AlterField(
            model_name='car',
            name='content',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=100, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='car',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='brand',
            field=models.CharField(default='неизвестно', max_length=10, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='photo',
            field=models.ImageField(upload_to='photos', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='city',
            field=models.CharField(max_length=10, verbose_name='Город'),
        ),
    ]
