from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Ticket, User


class TicketForm(forms.ModelForm):
    SUBJECT_CHOICES = (
        ('', 'موضوع:'),
        ('مشکل در سایت', 'مشکل درسایت'),
        ('درخواست نویسندگی', 'درخواست نویسندگی'),
        ('غیره', 'غیره')
    )

    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Ticket
        fields = ('subject', 'user', 'message')
        widgets = {
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'متن پیام'}
            )
        }

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False


class RegisterForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control mt-1'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mt-1'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mt-1'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mt-1'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mt-1'
        })

