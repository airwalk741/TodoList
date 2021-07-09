from rest_framework import routers, serializers
from .models import Article


class ArticleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        # read_only = 'user'
