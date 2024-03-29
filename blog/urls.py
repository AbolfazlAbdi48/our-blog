from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    HomePageView,
    CategoryList,
    like_article,
    save_article,
    CategoryDetails
)

app_name = 'blog'
urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('latest', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/<str:title>', ArticleDetailView.as_view(), name='article_detail'),
    path('categories', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>', CategoryDetails.as_view(), name='category_articles'),
    path('like/', like_article, name='like_article'),
    path('save/', save_article, name='save_article'),
]

# handler404 = 'blog.views.handeler_404'
