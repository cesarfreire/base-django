"""Views do app users."""
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

User = get_user_model()


# Create your views here.
@login_required()
def my_profile(request):
    """Just a example view do load users infos"""
    return render(request, 'account/profile.html')
