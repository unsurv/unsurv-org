from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Images
from django.template import loader
# Create your views here.


def index(request):

    raw_language_code = request.META.get("HTTP_ACCEPT_LANGUAGE")
    accepted_language = select_language(request.META.get("HTTP_ACCEPT_LANGUAGE"))

    latest_article_list = Article.objects.order_by('-publication_datetime')[:5]

    if accepted_language != "en":
        pass
    else:
        latest_article_list = Article.objects.order_by('-publication_datetime')[:5]

    # images = Images.objects.all()[0]

    context = {
        'language_preference': accepted_language,
        'latest_article_list': latest_article_list,
        'language_code': raw_language_code,
    }
    return render(request, 'website/index.html', context)


def detail(request, article_id):
    return HttpResponse("You're looking at article with id:  %s." % article_id)


def blog_overview(request):

    raw_language_code = request.META.get("HTTP_ACCEPT_LANGUAGE")
    accepted_language = select_language(request.META.get("HTTP_ACCEPT_LANGUAGE"))

    blog_overview_list = Article.objects.order_by('-publication_datetime')[:20]

    context = {
        'language_preference': accepted_language,
        'blog_overview_list': blog_overview_list,
        'language_code': raw_language_code,
    }

    return render(request, 'website/blog_overview.html', context)


def select_language(http_accept_language_string):
    if "de" in http_accept_language_string:
        return "de"
    else:
        return "en"
