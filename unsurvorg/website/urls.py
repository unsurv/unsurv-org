from django.urls import path

from . import views

urlpatterns = [
    # ex: unsurv.org
    path('', views.index, name='index'),

    # ex: /blog shows lates blog entries
    path('blog', views.blog_overview, name='blog_overview'),

    # ex: /blog/5/ TODO maybe remove this later
    path('blog/<int:article_id>/', views.detail, name='detail'),

    # ex: /blog/this-is-a-slug/
    path('blog/<slug:slug>/', views.detail_slug, name='detail_slug'),

    path('contact', views.contact, name='contact'),

    path('privacy', views.privacy, name='privacy'),

    path('info', views.info, name='info'),

]
