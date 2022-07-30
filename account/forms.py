from django import forms
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


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mt-1'}),
        max_length=150
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control mt-1'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-1'}),
        max_length=128
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-1'}),
        max_length=128
    )
    
