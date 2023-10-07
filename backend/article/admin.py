from django.contrib import admin
from article.models import Article, ArticleAdditionalColumn, ArticleAdditionalField

admin.site.register(Article)
admin.site.register(ArticleAdditionalColumn)
admin.site.register(ArticleAdditionalField)