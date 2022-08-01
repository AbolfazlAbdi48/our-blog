from django.urls import path

from .views import (
    author_view,
    SendTicket,
    UserDetailView,
    UserUpdateView,
    RegisterView,
    SignInView
)

app_name = 'account'

urlpatterns = [
    path('ticket/', SendTicket.as_view(), name='ticket_crete'),
    path('account/activity/', UserDetailView.as_view(), name='account_activity'),
    path('account/update/', UserUpdateView.as_view(), name='account_update'),
    path('register', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('<slug:username>/', author_view, name='author_detail'),
]
