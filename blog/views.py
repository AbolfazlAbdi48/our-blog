from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.db.models import Count
from .models import (
    Article,
    Category,
    Like,
    SaveArticle
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

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['liked'] = Like.objects.filter(article=self.object, owner=self.request.user)
        context['saved'] = SaveArticle.objects.filter(article=self.object, owner=self.request.user)
        return context

    template_name = 'blog/article_detail.html'
    context_object_name = 'article'


class HomePageView(ListView):
    paginate_by = 1
    model = Article
    query_set = Article.objects.filter(
        publish_time__lte=timezone.now()).order_by('-publish_time')[0:3]
    context_object_name = 'latest'
    template_name = 'blog/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['topusers'] = User.objects.filter(is_staff=True)[0: 2]
        context['categorys'] = Category.objects.all()[0: 19]
        context['latest2'] = Article.objects.all().order_by('hits')[0: 3]
        return context


def like_article(request):
    if request.method == "POST":
        article_id = request.POST['article_id']
        user = request.user

        try:
            like = Like.objects.get(article__id=article_id, owner=user)
            like.delete()
            return HttpResponse('like deleted')
        except Like.DoesNotExist:
            like = Like(article_id=article_id, owner=user)
            like.save()
            return HttpResponse('liked')

    raise Http404


def save_article(request):
    if request.method == "POST":
        # get data
        article_id = request.POST['article_id']
        user = request.user

        try:
            save_article = SaveArticle.objects.get(article__id=article_id, owner=user)
            save_article.delete()
            return HttpResponse('save deleted')
        except SaveArticle.DoesNotExist:
            save_article = SaveArticle(article_id=article_id, owner=user)
            save_article.save()
            return HttpResponse('saved')

    raise Http404
