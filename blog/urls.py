from django.urls import path
from .views import (
    ArticleListView
)


urlpatterns = [
    path('latest', ArticleListView.as_view(), name='article_list')  # ArticleListView
]
