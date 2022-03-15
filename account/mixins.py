from ast import arg
from django.http import Http404
from django.shortcuts import redirect


class AccountPagesMixin:
    """
    This mixin gives access to authenticated users.
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return redirect('/admin')
        elif request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        raise Http404
