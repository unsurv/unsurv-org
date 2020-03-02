from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article


# Create your views here.


def index(request):

    # get browser language preference
    raw_language_code = request.META.get("HTTP_ACCEPT_LANGUAGE")
    # choose from two languages for now
    accepted_language = select_language(raw_language_code)

    # get latest articles
    latest_article_list = Article.objects.order_by('-publication_datetime')[:5]

    top_article = Article.objects.get(keep_top_position=True)

    # TODO display german translation if de in accepted browser languages
    if accepted_language != "en":
        pass
    else:
        latest_article_list = Article.objects.order_by('-publication_datetime')[:5]

    # images = Images.objects.all()[0]

    context = {
        'language_preference': accepted_language,
        'top_article': top_article,
        'latest_article_list': latest_article_list,
        'language_code': raw_language_code,
    }
    return render(request, 'website/index.html', context)


# maybe remove finding articles with ids completely
def detail(request, article_id):
    return HttpResponse("You're looking at article with id:  %s." % article_id)


def detail_slug(request, slug):

    # get browser language preference
    raw_language_code = request.META.get("HTTP_ACCEPT_LANGUAGE")
    # choose from two languages for now
    accepted_language = select_language(raw_language_code)

    article = get_object_or_404(Article, slug=slug)

    context = {
        'language_preference': accepted_language,
        'article': article,
        'language_code': raw_language_code,
    }
    return render(request, 'website/detail.html', context)


def blog_overview(request):

    raw_language_code = request.META.get("HTTP_ACCEPT_LANGUAGE")
    accepted_language = select_language(raw_language_code)


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
