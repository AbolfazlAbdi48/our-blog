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
        if self.request.user.is_authenticated:
            context['liked'] = Like.objects.filter(
                article=self.object, owner=self.request.user).exists()
            context['saved'] = SaveArticle.objects.filter(
                article=self.object, owner=self.request.user).exists()
            context['liked'] = Like.objects.filter(article=self.object, owner=self.request.user).exists()
            context['saved'] = SaveArticle.objects.filter(article=self.object, owner=self.request.user).exists()
        return context

    template_name = 'blog/article_detail.html'
    context_object_name = 'article'


def home_page(request):
    most_viewed_articles = Article.objects.filter(
        publish_time__lte=timezone.now()
    ).order_by('-hits')

    latest_articles = Article.objects.filter(
        publish_time__lte=timezone.now()
    ).order_by('-id')[:4]

    categories = Category.objects.filter(is_active=True)

    popular_authors = most_viewed_articles.distinct()[:2]

    context = {
        'most_viewed': most_viewed_articles[:4],
        'latest': latest_articles,
        'categories': categories,
        'popular_authors': popular_authors
    }
    return render(request, 'blog/homepage.html', context)


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
            save_article = SaveArticle.objects.get(
                article__id=article_id, owner=user)
            save_article.delete()
            return HttpResponse('save deleted')
        except SaveArticle.DoesNotExist:
            save_article = SaveArticle(article_id=article_id, owner=user)
            save_article.save()
            return HttpResponse('saved')

    raise Http404
