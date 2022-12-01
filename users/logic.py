from django.contrib import auth, messages
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from products.models import Basket


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
        'title': 'Store - Войти',
        'form': form
    }
    return context


def register_page_context(form):
    context = {
        'title': 'Store - Регистрация',
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


def profile_page_context(form, user):
    baskets = Basket.objects.filter(user=user)
    total_quantity = sum(basket.quantity for basket in baskets)
    total_sum = sum(basket.sum() for basket in baskets)
    context = {
        'title': 'Store - Личный кабинет',
        'form': form,
        'baskets': baskets,
        'total_quantity': total_quantity,
        'total_sum': total_sum,
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
