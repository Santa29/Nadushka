from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(_("ФИО"), max_length=256)
    image = models.ImageField(_("Изображение"), upload_to="authors/")
    position = models.CharField(_("Должность"), max_length=256)
    description = models.CharField(_("Описание"), max_length=512, blank=True)
    slug = models.SlugField(_("Аббривеатура"), max_length=20, unique=True)
    istina_author_ref = models.CharField(_("Ссылка на сотрудника в системе истина"), max_length=160, unique=True)
    firstname = models.CharField(_("Имя на английском с заглавной буквы"), max_length=25)
    lastname = models.CharField(_("Фамилия на английском с заглавной буквы"), max_length=40)
    thirdname = models.CharField(_("Отчество на английском с заглавной буквы"), max_length=40)
    google_sholar_reference = models.CharField(_("Ссылка на сотрудника в системе Google Sholar"), max_length=160, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _("Автор")
        verbose_name_plural = _("Авторы")


class Article(models.Model):
    name = models.CharField(_("Название"), max_length=512)
    date = models.DateField(_("Дата написания"), null=True, blank=True)
    authors = models.ManyToManyField(Author, verbose_name='Авторы', related_name='article_authors', blank=True)
    url = models.CharField(max_length=160, unique=True, blank=True)
    journal = models.CharField(_("Журнал"), max_length=512)
    abstract = models.TextField(_("Абстракт"), blank=True)
    istina_article_id = models.CharField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")
        ordering = ["date"]

class Post(models.Model):
    head = models.CharField(max_length=512)
    body = models.TextField()
    image = models.ImageField("Картинка", upload_to="images/")