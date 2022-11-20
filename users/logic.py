from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from users.forms import UserRegistrationForm


def authenticate(request, form):
    """
    Validate the form and if it correctly filled then authenticate User
    args: request, form
    after: performs authorization
    """
    # authenticate
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # authorization
        authorizate(user, request)


def authorizate(user, request):
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
    return valut type
    """
    context = {
        'form': form
    }
    return context


def register_page_context():
    context = {
        'form': get_register_form()
    }
    return context


def get_register_form():
    return UserRegistrationForm
