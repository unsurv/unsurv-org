from django.db import models

from django.utils import timezone
import datetime

# Create your models here.


class Article(models.Model):
    language = models.CharField(max_length=2, default="en")
    title = models.CharField(max_length=200)
    text = models.TextField()
    abstract = models.CharField(max_length=360, default="")
    embedded_video_url = models.URLField(blank=True)
    text_after_media = models.TextField(blank=True, default="")
    keep_top_position = models.BooleanField(default=False)

    publication_datetime = models.DateTimeField("date_published")
    last_updated_datetime = models.DateTimeField("last_updated", auto_now=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.publication_datetime >= timezone.now() - datetime.timedelta(days=1)


class TranslatedArticle(models.Model):
    article = models.ForeignKey(Article, related_name="translations", on_delete="CASCADE")
    language = models.CharField(max_length=2)
    title = models.CharField(max_length=200)
    text = models.TextField()
    abstract = models.CharField(max_length=360, default="")
    embedded_video_url = models.URLField(blank=True)
    text_after_video = models.TextField(blank=True, default="")
    keep_top_position = models.BooleanField(default=False)

    publication_datetime = models.DateTimeField("date_published")
    last_updated_datetime = models.DateTimeField("last_updated", auto_now=True)

    def __str__(self):
        return self.article_title


class Images(models.Model):
    article = models.ForeignKey(Article, related_name="images", on_delete="CASCADE")

    low_res = models.ImageField(blank=True, upload_to="images/low_res")
    high_res = models.ImageField(blank=True, upload_to="images/high_res")




"""
add Article in shell and create it


from website.models import Article
a = Article(article_title = "Lorem Ipsum2",  article_text="Atque qui laboriosam et ex. Nihil suscipit omnis sed fuga quis. Ducimus hic et et autem quo qui est pariatur. Ullam ab commodi repudiandae voluptas iure. Omnis laudantium ratione ut. Sint facere commodi voluptatem. Consequuntur quas officia eaque nemo. Doloremque in inventore qui quia est ullam et. Illum molestias voluptas perspiciatis quos reiciendis molestiae adipisci dicta. Eum quia vitae modi molestiae. Hic consequatur voluptates vel molestias error ut perspiciatis.",
            publication_datetime=timezone.now(),
            last_updated_datetime=timezone.now())
            
a.save()

"""
