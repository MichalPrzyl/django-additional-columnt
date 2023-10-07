from django.db import models
from django.contrib.contenttypes.models import ContentType

class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()


class AdditionalColumn(models.Model):
    corresponding_table = models.ForeignKey(ContentType, related_name='additionals', on_delete=models.CASCADE)
    instance_id = models.IntegerField()
    field_1_name = models.CharField(max_length=255)
    field_1_value = models.CharField(max_length=255, null=True)
    
