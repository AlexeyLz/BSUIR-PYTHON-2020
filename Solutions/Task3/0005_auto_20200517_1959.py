# Generated by Django 3.0.6 on 2020-05-17 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cars', '0004_auto_20200517_1149'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarImage',
        ),
        migrations.DeleteModel(
            name='Salon',
        ),
        migrations.AddField(
            model_name='car',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец объявления'),
        ),
    ]