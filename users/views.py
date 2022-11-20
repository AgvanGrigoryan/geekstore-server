from django.shortcuts import render

from users.forms import UserLoginForm
from users.logic import authenticate, login_page_context, register_page_context


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        authenticate(request, form)
    else:
        form = UserLoginForm()
    context = login_page_context(form)
    return render(request, 'users/login.html', context)


def register(request):
    context = register_page_context()
    return render(request, 'users/register.html', context)
