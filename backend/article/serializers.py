from rest_framework import serializers
# models
from article.models import Article, ArticleAdditionalColumn

# write standard modelsserializer for model article.Article
class ArticleAdditionalColumnSerialzier(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = ArticleAdditionalColumn
        fields = '__all__'
    
    # def get_value(self, instance):

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def get_fields(self):
        from django.db.models.fields import Field
        fields = super().get_fields()
        my_field = Field('abc')
        # fields[my_field] = 'eklo'

        return fields

        
class BaseArticleSerializer(serializers.BaseSerializer):
    # additional_fields = serializers.SerializerMethodField()
    def to_representation(self, instance):
        data = {}
        for additional_field in instance.additional_fields.all():
            data[additional_field.column.name] = additional_field.value
        serializer = ArticleSerializer(instance)
        
        return {**data, **serializer.data}
        
    class Meta:
        model = Article
        fields = '__all__'

    # def get_additional_fields(self, instance):
        # qs = ArticleAdditionalColumn.objects.all()
        # serializer = ArticleAdditionalColumnSerialzier(qs, many=True)
        # return serializer.data