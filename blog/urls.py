from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    HomePageView,
    like_article,
    save_article
)


urlpatterns = [
    path('latest', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/<str:title>', ArticleDetailView.as_view(), name='article_detail'),
    path('', HomePageView.as_view(), name='home_page'),
    path('like/', like_article, name='like_article'),
    path('save/', save_article, name='save_article'),
]
