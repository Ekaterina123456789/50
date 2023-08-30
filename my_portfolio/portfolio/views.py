from django.shortcuts import render, redirect, get_object_or_404
from .models import Catalog
from .forms import WorkForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ViewForm


def portfolio(request):
    works = Catalog.objects.all()
    return render(request, 'userpage/works.html', {'works': works})


def add_work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = WorkForm()
    return render(request, 'userpage/add_work.html', {'form': form})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'userpage/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('viewfavourite')
            except IntegrityError:
                return render(request, 'userpage/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует! Попробуйте другое'})
        else:
            return render(request, 'userpage/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпали!'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'userpage/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'userpage/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('viewfavourite')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('works')


@login_required
def viewfavourite(request):
    works = Catalog.objects.filter(user=request.user)
    return render(request, 'userpage/viewfavourite.html', {'works': works})
