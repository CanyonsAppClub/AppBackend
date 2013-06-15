from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.shortcuts import render

def home(request):
    return render(request, 'welcome.html')
