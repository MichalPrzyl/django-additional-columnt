from typing import Any
from django.db import models
from django.contrib.contenttypes.models import ContentType

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


from django.db.models import CharField
from django.db.models.signals import class_prepared


class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
   
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

class ArticleAdditionalColumn(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class ArticleAdditionalField(models.Model):
    column = models.ForeignKey(ArticleAdditionalColumn, on_delete=models.CASCADE)
    instance = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='additional_fields') 
    value = models.CharField(max_length=255)



# @receiver(pre_save, sender=Article)
@receiver(post_save, sender=ArticleAdditionalColumn)
# def lol(sender, instance, *args, **kwargs):
def lol(instance, created, **kwargs):
    if created:
        all_articles = Article.objects.all()
        for article in all_articles:
            data = {
                'column': instance,
                'instance': article,
                'value': ''
            }
            ArticleAdditionalField.objects.create(**data)
      
@receiver(post_save, sender=Article)
def create_additional_value(instance, created, **kwargs):
    if created:
        for column in ArticleAdditionalColumn.objects.all():
            data = {
                    'column': column,
                    'instance': instance,
                    'value': ''
                }
            ArticleAdditionalField.objects.create(**data)

