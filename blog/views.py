from django.shortcuts import render
from django.views.generic import ListView
from .models import (
    Article
)

# Create your views here.


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.order_by('-publish_time')
    context_object_name = 'articles'
    template_name = 'blog/article_list.html'

