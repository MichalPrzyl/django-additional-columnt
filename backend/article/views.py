from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
# models
from article.models import Article
# serializers
from article.serializers import ArticleSerializer
# forms
from article.forms import ArticleForm

class ArticleAPI(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects


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

