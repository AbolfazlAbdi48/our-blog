from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, View, UpdateView
from django.contrib import messages

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
        messages.success(self.request, 'تیکت شما با موفقیت ارسال شد.')
        return super().form_invalid(form)


class UserDetailView(View):
    template = 'account/account.html'

    def get(self, request):
        context = {
            'user_data': User.objects.get(username=request.user.username)
        }
        return render(request, self.template, context)


class UserUpdateView(UpdateView):
    def get_object(self):
        request = self.request
        user = get_object_or_404(User, username=request.user.username)
        return user

    template_name = 'account/account_update.html'
    success_url = reverse_lazy('account:account_activity')
    fields = ('username', 'email', 'first_name', 'last_name', 'avatar')
