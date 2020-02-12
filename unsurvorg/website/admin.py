from django.contrib import admin

# Register your models here.

from .models import Article, TranslatedArticle

admin.site.register(Article)
admin.site.register(TranslatedArticle)
