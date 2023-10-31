from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from allauth.account.forms import LoginForm

User = get_user_model()


# Create your views here.
@login_required()
def my_profile(request):
    return render(request, 'account/profile.html')
