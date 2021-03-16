from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('service')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('service')
            else:
                messages.add_message(request, messages.INFO, 'Username or Password is incorrect')

        context = {

        }
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('service')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.add_message(request, messages.SUCCESS,'Account was created with username: ' + user)
                return redirect('login')
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)

