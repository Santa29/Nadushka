from django.contrib import admin
from posts.models import Author, Article, Post

# Register your models here.
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Post)