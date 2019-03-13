from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time', 'id')
    list_filter = ('time',)

admin.site.register(Article, ArticleAdmin)