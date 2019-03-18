from django.contrib import admin
from .models import Article
from .models import CurUser
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time', 'id')
    list_filter = ('time',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(CurUser)
admin.site.register(models.ExampleModel)