from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
# models
from article.models import Article, ArticleAdditionalColumn, ArticleAdditionalField
# serializers
from article.serializers import ArticleSerializer, BaseArticleSerializer
# forms
from article.forms import ArticleForm
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

class OwnFilterBackend(DjangoFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        output = []
        print('lul')
        for element in request.GET.keys():
            additional_column = element
            additional_value = request.GET[element]
            fields = ArticleAdditionalField.objects.filter(instance__in=queryset.all(), 
                                                           column__name=additional_column,
                                                           value=additional_value)\
                                                            .values_list('instance_id', flat=True)

            output.extend(fields)

        qs = queryset.filter(id__in=output)
        print(f"\033[94mqs\033[0m: {qs}")
        return qs


# class ArticleFilter(django_filters.FilterSet):
#     id = django_filters.NumberFilter()
#     class Meta:
#         model = Article
#         fields = ['id']


class ArticleAPI(generics.ListAPIView):
    serializer_class = BaseArticleSerializer
    queryset = Article.objects
    filter_backends = [OwnFilterBackend]
    filterset_fields = ['id']




from django.http import HttpResponse
from django.template import loader
from django.template.loader import render_to_string
from django.shortcuts import render
def articles(request):
    template = loader.get_template('articles.html')
    # get all instances of ARticle model
    all_articles=Article.objects.all().values()
    context = {
        "data": all_articles,
        'form': ArticleForm.as_table(), 
    }

    # rendered = render_to_string("articles.html", context)
    rendered = render(request, "articles.html", context)
    # return HttpResponse(template.render())
    return HttpResponse(rendered)

        
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            print(f"\033[94mform.__dict__\033[0m: {form.__dict__}")
            form.save()
            return HttpResponse("/thanks/")
        # print(f"\033[94mrequest.body\033[0m: {request.body}")
        # print("this is post method")
        return HttpResponse("abc")

