from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template import loader
# Create your views here.


def index(request):
    latest_article_list = Article.objects.order_by('-publication_datetime')[:5]
    template = loader.get_template('website/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, article_id):
    return HttpResponse("You're looking at article with id:  %s." % article_id)