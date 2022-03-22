from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.db.models import Count
from .models import (
    Article,
    Category
)

from account.models import User

# Create your views here.

def count_of_object(object):
    return Count(object)


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(
        publish_time__lte=timezone.now()).order_by('-publish_time')
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


class HomePageView(ListView):
    paginate_by = 1
    model = Article
    query_set = Article.objects.filter(publish_time__lte=timezone.now()).order_by('-publish_time')[0:3]
    context_object_name = 'latest'
    template_name = 'blog/homepage.html'

    def get_context_data(self,**kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        context['topusers'] = User.objects.filter(is_staff=True)[0: 2]
        context['categorys'] = Category.objects.all()[0: 19]
        context['latest2'] = Article.objects.all().order_by('hits')[0: 3]
        return context
    
