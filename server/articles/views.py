from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article
from .serializers import ArticleSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST', 'GET'])
def index(request):

    if request.method == 'POST':
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
    else:
        articles = Article.objects.order_by('-pk')
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data, status=200)


@api_view(['PUT', 'GET', 'DELETE'])
def detail(request, article_pk):
    
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializers(article)
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        article.delete()
        # Postman 확인하기 위해 data 쓴거임 
        data = {
            'pk': str(article_pk) + '번 게시물 삭제 완료'  
        }
        return Response(data, status=200)
    elif request.method == 'PUT':
        serializer = ArticleSerializers(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

