from rest_framework import serializers
# models
from article.models import Article

# write standard modelsserializer for model article.Article
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'