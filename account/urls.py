from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    author_view,
    SendTicket,
    UserDetailView
)

urlpatterns = [
    path('ticket/', SendTicket.as_view(), name='ticket_crete'),
    path('<slug:username>/', author_view, name='author_detail'),
    path('account/activity/', login_required(UserDetailView.as_view()), name='account_activity')
]