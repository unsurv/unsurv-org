from django.urls import path

from . import views

urlpatterns = [
    # ex: unsurv.org
    path('', views.index, name='index'),

    path('blog', views.blog_overview, name='blog_overview'),

    # ex: /blog/5/
    path('blog/<int:article_id>/', views.detail, name='detail'),

]
