from django.urls import path

from .views import (
    author_view

)

urlpatterns = [
    path('<slug:username>/', author_view, name='author_detail')
]
