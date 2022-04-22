from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    home_page,
    like_article,
    save_article
)

app_name = 'blog'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('latest', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/<str:title>', ArticleDetailView.as_view(), name='article_detail'),
    path('like/', like_article, name='like_article'),
    path('save/', save_article, name='save_article'),
]
