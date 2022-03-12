from django import forms
from .models import Ticket


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
