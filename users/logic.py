from django.contrib import auth
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


def save_new_user_in_db(form):
    """
        Validate the form and if it correctly filled then Save User in Database
        return: HttpResponseRedirect(reverse('index'))
    """
    form.save()
    return HttpResponseRedirect(reverse('users:login'))
    # else:
    #     print(form.errors)

def edit_user_data_in_db(form):
    form.save()
    return HttpResponseRedirect(reverse('users:profile'))

def profile_page_context(form):
    context = {
        'form': form,
    }
    return context