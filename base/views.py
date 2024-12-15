from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import SignUpForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def registerPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'signup.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('home')


def loginPage(request):

    if request.method == 'POST':
        CPF = request.POST['CPF']
        password = request.POST['password']

        user = authenticate(request, CPF=CPF, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid CPF or password.')

    return render(request, 'login.html')