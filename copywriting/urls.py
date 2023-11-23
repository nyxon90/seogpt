from django.urls import path
from copywriting.views import copywriting, copywriting_articles, article_detail


urlpatterns = [
    path('', copywriting, name=''),
    path('create_article', copywriting, name='create_article'),
    path('articles', copywriting_articles, name='articles'),
    path('articles/<int:article_id>/', article_detail, name='article_detail'),
]