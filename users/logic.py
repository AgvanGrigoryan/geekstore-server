from django.contrib import auth, messages
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def authenticate(request):
    """
    Validate the form and if it correctly filled then authenticate User
    args: request, form
    after: performs authorization
    """
    # authenticate
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    return user


def authorizate(request, user):
    """
    Login User if him is active and correct
    args: user, request
    return: HttpResponseRedirect(reverse('index'))
    """
    if user and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('index'))


def login_page_context(form):
    """
    return login page context
    return value type
    """
    context = {
        'form': form
    }
    return context


def register_page_context(form):
    context = {
        'form': form
    }
    return context


def save_new_user_in_db(request, form):
    """
        if form correctly filled then Create new User in Database
        return: HttpResponseRedirect(reverse('users:login'))
    """
    form.save()
    messages.success(request, "Вы успешно зарегистрировались")
    return HttpResponseRedirect(reverse('users:login'))
    # else:
    #     print(form.errors)


def edit_user_data_in_db(form):
    """
        if form correctly filled then edit User datas in Database
        return: HttpResponseRedirect(reverse('users:login'))
     """
    form.save()
    return HttpResponseRedirect(reverse('users:profile'))


def profile_page_context(form):
    context = {
        'form': form,
    }
    return context


def logout_user(request):
    """
    Logout User on web-site
    args: request
    return: HttpResponseRedirect(reverse('index'))
    """
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
