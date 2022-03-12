from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from blog.models import (
    Article
)

from .models import (
    User
)


# Create your views here.

def author_view(request, username):
    print(username)
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
        'user_articles': user.articles.filter(publish_time__lte=timezone.now())
    }
    return render(request, 'account/author_articles.html', context=context)
