from django.contrib import admin

# Register your models here.

from .models import Article, TranslatedArticle, Images

admin.site.register(Article)
admin.site.register(TranslatedArticle)
admin.site.register(Images)
