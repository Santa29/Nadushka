# Generated by Django 3.1.2 on 2020-10-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201018_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='abbr',
            field=models.CharField(blank=True, max_length=20, verbose_name='Аббривеатура'),
        ),
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.CharField(blank=True, max_length=512, verbose_name='Описание'),
        ),
    ]
