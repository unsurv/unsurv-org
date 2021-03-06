from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, TranslatedArticle
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# TODO button to choose language


def index(request):

    # get browser language preference
    raw_http_accept = request.META.get("HTTP_ACCEPT_LANGUAGE")
    # choose from two languages for now

    # default to "en"
    if raw_http_accept:
        language_preference = select_language(raw_http_accept)
    else:
        language_preference = "en"

    # get latest articles

    # TODO later query if translations for preference is available for now only two languages will be supported (de/en)
    if language_preference == "de":

        latest_article_list = TranslatedArticle.objects.filter(language=language_preference) \
                                  .exclude(is_info_page=True) \
                                  .order_by('-publication_datetime')[:5]

        top_article = TranslatedArticle.objects.filter(language=language_preference) \
            .get(keep_top_position=True)
    else:
        top_article = Article.objects.get(keep_top_position=True)
        latest_article_list = Article.objects.exclude(is_info_page=True).order_by('-publication_datetime')[:5]

    context = {
        'language_preference': language_preference,
        'top_article': top_article,
        'latest_article_list': latest_article_list,
        'language_code': raw_http_accept,
    }

    return render(request, 'website/index.html', context)


# maybe remove finding articles with ids completely
def detail(request, article_id):
    return HttpResponse("You're looking at article with id:  %s." % article_id)


def detail_slug(request, slug):

    # get browser language preference
    raw_http_accept = request.META.get("HTTP_ACCEPT_LANGUAGE")
    # choose from two languages for now
    # default to "en"
    if raw_http_accept:
        language_preference = select_language(raw_http_accept)
    else:
        language_preference = "en"
    try:
        article = Article.objects.get(slug=slug)
    except ObjectDoesNotExist:
        article = get_object_or_404(TranslatedArticle, slug=slug)


    available_slugs = {}


    try:
        original_article = Article.objects.get(slug=slug)

    except ObjectDoesNotExist:
        # current article is a translated one, get original
        original_article = TranslatedArticle.objects.get(slug=slug).article

    available_slugs["en"] = original_article.slug

    translated_articles = original_article.translations.all()

    for translation in translated_articles:
        available_slugs[translation.language] = translation.slug

    context = {
        'language_preference': language_preference,
        'translations': available_slugs,
        'article': article,
        'language_code': raw_http_accept,
    }

    return render(request, 'website/detail.html', context)


def blog_overview(request):

    raw_http_accept = request.META.get("HTTP_ACCEPT_LANGUAGE")
    # default to "en"
    if raw_http_accept:
        language_preference = select_language(raw_http_accept)
    else:
        language_preference = "en"

    if language_preference == "de":

        blog_overview_list = TranslatedArticle.objects.filter(language=language_preference) \
                                 .exclude(is_info_page=True) \
                                 .order_by('-publication_datetime')[:20]

    else:
        blog_overview_list = Article.objects.exclude(is_info_page=True).order_by('-publication_datetime')[:20]

    context = {
        'language_preference': language_preference,
        'blog_overview_list': blog_overview_list,
        'language_code': raw_http_accept,
    }

    return render(request, 'website/blog_overview.html', context)


# TODO combine contact + privacy to single function
def contact(request):
    raw_http_accept = request.META.get("HTTP_ACCEPT_LANGUAGE")
    # default to "en"
    if raw_http_accept:
        language_preference = select_language(raw_http_accept)
    else:
        language_preference = "en"

    if language_preference == "de":

        info_article = TranslatedArticle.objects.filter(language=language_preference) \
                                 .get(title="contact")

    else:
        info_article = Article.objects.get(title="contact")

    context = {
        'language_preference': language_preference,
        'info': info_article,
        'language_code': raw_http_accept,
    }

    return render(request, 'website/info_template.html', context)


def privacy(request):
    raw_http_accept = request.META.get("HTTP_ACCEPT_LANGUAGE")
    # default to "en"
    if raw_http_accept:
        language_preference = select_language(raw_http_accept)
    else:
        language_preference = "en"

    if language_preference == "de":

        info_article = TranslatedArticle.objects.filter(language=language_preference) \
                                 .get(title="privacy")

    else:
        info_article = Article.objects.get(title="privacy")

    context = {
        'language_preference': language_preference,
        'info': info_article,
        'language_code': raw_http_accept,
    }

    return render(request, 'website/info_template.html', context)


def info(request):
    raw_http_accept = request.META.get("HTTP_ACCEPT_LANGUAGE")
    # default to "en"
    if raw_http_accept:
        language_preference = select_language(raw_http_accept)
    else:
        language_preference = "en"

    if language_preference != "en":

        info_article = get_object_or_404(TranslatedArticle, language= language_preference, slug="info")

    else:
        info_article = get_object_or_404(Article, language= language_preference, slug="info")

    context = {
        'language_preference': language_preference,
        'info': info_article,
        'language_code': raw_http_accept,
    }

    return render(request, 'website/info_template.html', context)


# expand if more translations available
def select_language(http_accept_language_string):
    if "de" in http_accept_language_string:
        return "de"
    else:
        return "en"
