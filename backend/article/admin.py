from django.contrib import admin
from article.models import Article, AdditionalColumn


admin.site.register(Article)
admin.site.register(AdditionalColumn)