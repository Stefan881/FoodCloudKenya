from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.
def home(request):
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('/')
