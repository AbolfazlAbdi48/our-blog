from django.urls import path

from .views import (
    author_view,
    SendTicket
)

urlpatterns = [
    path('ticket/', SendTicket.as_view(), name='ticket_crete'),
    path('<slug:username>/', author_view, name='author_detail'),
]
