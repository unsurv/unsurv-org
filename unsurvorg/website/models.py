from django.db import models

from django.utils import timezone
import datetime

# Create your models here.


class Article(models.Model):
    article_language = models.CharField(max_length=2, default="en")
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    embedded_video_url = models.URLField()
    text_after_video = models.TextField(default="")
    keep_top_position = models.BooleanField(default=False)

    publication_datetime = models.DateTimeField("date_published", auto_now=True)
    last_updated_datetime = models.DateTimeField("last_updated", auto_now=True)

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.publication_datetime >= timezone.now() - datetime.timedelta(days=1)


class TranslatedArticle(models.Model):
    article = models.ForeignKey(Article, related_name="translations", on_delete="CASCADE")
    article_language = models.CharField(max_length=2)
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    embedded_video_url = models.URLField()
    text_after_video = models.TextField(default="")
    keep_top_position = models.BooleanField(default=False)

    publication_datetime = models.DateTimeField("date_published", auto_now=True)
    last_updated_datetime = models.DateTimeField("last_updated", auto_now=True)



"""
add Article in shell and create it


from website.models import Article
a = Article(article_title = "Lorem Ipsum2",  article_text="Atque qui laboriosam et ex. Nihil suscipit omnis sed fuga quis. Ducimus hic et et autem quo qui est pariatur. Ullam ab commodi repudiandae voluptas iure. Omnis laudantium ratione ut. Sint facere commodi voluptatem. Consequuntur quas officia eaque nemo. Doloremque in inventore qui quia est ullam et. Illum molestias voluptas perspiciatis quos reiciendis molestiae adipisci dicta. Eum quia vitae modi molestiae. Hic consequatur voluptates vel molestias error ut perspiciatis.",
            publication_datetime=timezone.now(),
            last_updated_datetime=timezone.now())
            
a.save()

"""
