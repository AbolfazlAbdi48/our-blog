from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    HomePageView,
    CategoryList,
    # home_page,
    like_article,
    save_article
)

app_name = 'blog'
urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('latest', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/<str:title>', ArticleDetailView.as_view(), name='article_detail'),
    path('categories', CategoryList.as_view(), name='categories'),
    path('like/', like_article, name='like_article'),
    path('save/', save_article, name='save_article'),
]
