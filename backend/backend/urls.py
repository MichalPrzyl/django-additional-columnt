from django.contrib import admin
from django.urls import path
# views

from article.views import ArticleAPI, articles, article_create



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articles', ArticleAPI.as_view())
    path('articles/', articles, name='articles'),
    path('articles/create', article_create, name='articles_create'),
    # add path for article
]
