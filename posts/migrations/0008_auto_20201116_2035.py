# Generated by Django 3.1.2 on 2020-11-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20201022_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='istina_article_id',
            field=models.CharField(blank=True, max_length=160, unique=True),
        ),
        migrations.AddField(
            model_name='author',
            name='istina_author_id',
            field=models.CharField(blank=True, max_length=160, unique=True),
        ),
    ]