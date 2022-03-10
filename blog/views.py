from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import (
    Article
)

# Create your views here.


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.order_by('-publish_time')
    context_object_name = 'articles'
    template_name = 'blog/article_list.html'


class ArticleDetailView(DetailView):
    def get_object(self):
        article_id = self.kwargs.get('pk')
        article = get_object_or_404(
            Article, pk=article_id, publish_time__lte=timezone.now()
        )
        return article

    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
