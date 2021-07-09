from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article
from .serializers import ArticleSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST', 'GET'])
def index(request):

    if request.method == 'POST':
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        articles = Article.objects.order_by('-pk')
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

