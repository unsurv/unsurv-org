from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, TranslatedArticle
from django.template import loader
# Create your views here.


def index(request):

    raw_language_code = request.META.get("HTTP_ACCEPT_LANGUAGE")
    website_language = select_language(request.META.get("HTTP_ACCEPT_LANGUAGE"))

    if website_language != "en":
        latest_article_list = TranslatedArticle.objects \
                                  .filter(article_language=website_language) \
                                  .order_by('-publication_datetime')[:5]

        if len(latest_article_list) == 0:
            latest_article_list = Article.objects.order_by('-publication_datetime')[:5]

    else:
        latest_article_list = Article.objects.order_by('-publication_datetime')[:5]



    context = {
        'latest_article_list': latest_article_list,
        'language_code': raw_language_code,
    }
    return render(request, 'website/index.html', context)


def detail(request, article_id):
    return HttpResponse("You're looking at article with id:  %s." % article_id)


def select_language(http_accept_language_string):
    if "de" in http_accept_language_string:
        return "de"
    else:
        return "en"
