from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from blog.models import (
    Article
)
from .forms import TicketForm
from .models import (
    User,
    Ticket
)


# Create your views here.

def author_view(request, username):
    print(username)
    user = get_object_or_404(User, username=username, is_staff=True)
    context = {
        'user': user,
        'user_articles': user.articles.filter(publish_time__lte=timezone.now())
    }
    return render(request, 'account/author_articles.html', context=context)


class SendTicket(CreateView):
    model = Ticket()
    template_name = 'account/ticket_create.html'
    form_class = TicketForm

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.user = self.request.user
        ticket.save()
        return super().form_invalid(form)
