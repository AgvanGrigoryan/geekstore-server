from django.shortcuts import render

from users.forms import UserLoginForm, UserRegistrationForm
from users.logic import authenticate, login_page_context, register_page_context, save_new_user_in_db


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        authenticate(request, form)
    else:
        form = UserLoginForm()
    context = login_page_context(form)
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        save_new_user_in_db(form)
    else:
        form = UserRegistrationForm()
    context = register_page_context(form)
    return render(request, 'users/register.html', context)
