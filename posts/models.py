from django.db import models
from django.utils import timezone

from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField("ФИО", max_length=256)
    image = models.ImageField("Изображение", upload_to="authors/")
    position = models.CharField("Должность", max_length=256)
    description = models.CharField("Описание", max_length=512, blank=True)
    slug = models.SlugField("Аббривеатура", max_length=20, unique=True)
    istina_author_ref = models.CharField("Ссылка на сотрудника", max_length=160, unique=True)
    firstname = models.CharField("Имя", max_length=25)
    lastname = models.CharField("Фамилия", max_length=40)
    thirdname = models.CharField("Отчество", max_length=40)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"



class Article(models.Model):
    name = models.CharField("Название", max_length=512)
    date = models.DateField("Дата написания", null=True, blank=True)
    authors = models.ManyToManyField(Author, verbose_name='Авторы', related_name='article_authors', blank=True)
    url = models.CharField(max_length=160, unique=True, blank=True)
    journal = models.CharField("Журнал", max_length=512)
    abstract = models.TextField("Абстракт", blank=True)
    istina_article_id = models.CharField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["date"]

class Post(models.Model):
    head = models.CharField(max_length=512)
    body = models.TextField()
    image = models.ImageField("Картинка", upload_to="images/")