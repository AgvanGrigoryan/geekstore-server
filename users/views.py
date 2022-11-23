from django.shortcuts import render

from users.forms import UserLoginForm, UserRegistrationForm
from users.logic import authenticate, login_page_context, register_page_context, save_new_user_in_db, authorizate


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, form)
            return authorizate(request, user)
        print(form.errors)
    else:
        form = UserLoginForm()
    context = login_page_context(form)
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            return save_new_user_in_db(form)
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = register_page_context(form)
    return render(request, 'users/register.html', context)
