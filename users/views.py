from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    context = {
        'title': 'Авторизация в Geek Shop',
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context['form'] = form
    return render(request, 'users/login.html', context=context)


def registration(request):
    context = {
        'title': 'Регистрация в Geek Shop',
    }
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context['form'] = form
    return render(request, 'users/register.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            messages.error(request, 'Профиль не обновлен')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)


    context = {
        'title': 'Профиль',
        'form': form,
        'basket': Basket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
