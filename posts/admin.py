from django.contrib import admin
from posts.models import Author, Article, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('abbr',)}
    
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Post)