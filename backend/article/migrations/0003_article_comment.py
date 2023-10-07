# Generated by Django 4.2.6 on 2023-10-07 16:36

from django.db import migrations, models


def forward_func(apps, schema_editor):
    from django.db.models import F
    from django.db.models import Value as V
    from django.db.models.functions import Concat

    Article = apps.get_model('article.Article')
    Article.objects.all().update(comment=Concat(V("ID: "), F('id')))

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.CharField(default=1, max_length=255, null=True),
            preserve_default=False,
        ),

        migrations.RunPython(forward_func, reverse_func),

        # migrations.AddField(
        #     model_name='article',
        #     name='comment',
        #     field=models.CharField(default=1, max_length=255),
        #     preserve_default=False,
        # ),
        migrations.AlterField(
            model_name='article',
            name='comment',
            field=models.CharField(max_length=255)
        ),
    ]
