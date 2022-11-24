from django.shortcuts import render

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.logic import authenticate, login_page_context, register_page_context, save_new_user_in_db, authorizate, \
    profile_page_context, edit_user_data_in_db, logout_user


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request)
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
            return save_new_user_in_db(request, form)
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = register_page_context(form)
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            return edit_user_data_in_db(form)
    else:
        form = UserProfileForm(instance=request.user)
    context = profile_page_context(form)
    return render(request, 'users/profile.html', context)


def logout(request):
    return logout_user(request)
