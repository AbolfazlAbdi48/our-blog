from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView
)


urlpatterns = [
    path('latest', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/<str:title>', ArticleDetailView.as_view(), name='article_detail'),
]
