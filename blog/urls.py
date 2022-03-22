from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    HomePageView
)


urlpatterns = [
    path('latest', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/<str:title>', ArticleDetailView.as_view(), name='article_detail'),
    path('', HomePageView.as_view())
]
