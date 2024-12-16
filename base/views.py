from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse

from .models import User, InvestmentOption, InsuranceOption
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')

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

@login_required(login_url='login')
def depositPage(request):
    if request.method == 'POST':
        try:
            deposit_amount = request.POST['deposit_amount']

            if deposit_amount == '':
                raise ValueError('Insert the values correctly.')

            if(float(deposit_amount) <= 0):
                raise ValueError('Only positive values accepted.')

            request.user.balance += Decimal(deposit_amount)
            request.user.score = min(10.00, Decimal(deposit_amount)/1000 + request.user.score)
            request.user.save()

            messages.error(request, 'Deposit succeded.')

            return redirect('home')
        except ValueError as e:
            messages.error(request, e)

    return render(request, 'deposit.html')

@login_required(login_url='login')
def transferPage(request):
    if request.method == 'POST':
        try:
            destiny_cpf = request.POST['destiny_cpf']
            transfer_amount = request.POST['transfer_amount']

            if destiny_cpf == '' or transfer_amount == '':
                raise ValueError('Insert the values correctly.')

            destiny_user = get_object_or_404(User, CPF=destiny_cpf)

            if(Decimal(request.user.balance) < float(transfer_amount)):
                raise ValueError('Balance is less than value.')

            request.user.balance -= Decimal(transfer_amount)
            request.user.score = min(10.00, Decimal(transfer_amount)/1000 + request.user.score)
            destiny_user.balance += Decimal(transfer_amount)

            request.user.save()
            destiny_user.save()
            
            messages.error(request, 'Tranfer succeded.')

            return redirect('home')
        except ValueError  as e:
            messages.error(request, e)
        except Http404 as he:
            messages.error(request, 'No user found with given CPF.')

    return render(request, 'transfer.html')

@login_required(login_url='login')
def investmentPage(request):
    context = {
            'options': InvestmentOption.objects.all()
        }
    
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity'))
            option_id = request.POST.get('option_id')

            option = InvestmentOption.objects.get(id=option_id)

            if (quantity > option.quantity):
                raise ValueError('Quantity greater than avaiable.')

            total_value = Decimal(quantity) * Decimal(option.price)

            if total_value > request.user.balance:
                raise ValueError('Balance is less than total value.')
            
            request.user.balance -= total_value
            option.quantity -= quantity
            request.user.save()
            option.save()

            messages.success(request, 'Investment succed.')

            return redirect('home')
        except ValueError as e:
            messages.error(request, e)

    return render(request, 'investment.html', context)

@login_required(login_url='login')
def insurancePage(request):
    category = request.GET.get('category', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 99999999)
    min_score = request.GET.get('min_score', 10)

    options = InsuranceOption.objects.all()
    
    if category:
        options = options.filter(category__icontains=category)  # busca parcial de texto
    if min_price:
        options = options.filter(price__gte=min_price)
    if max_price:
        options = options.filter(price__lte=max_price)
    if min_score:
        options = options.filter(min_score__lte=min_score)

    context = {
        'options': options
    }

    if request.method == 'POST':
        try:
            option_id = request.POST.get('option_id')

            user = request.user
            option = InsuranceOption.objects.get(id=option_id)

            if(user.balance < option.price):
                raise ValueError('Balance is less than value.')

            if(user.score < option.min_score):
                raise ValueError('Minimum score was not reached.')

            request.user.balance -= InsuranceOption.objects.get(id=option_id).price
            request.user.save()

            return redirect('home')
        
        except ValueError as e:
            messages.error(request, e)

    return render(request, 'insurance.html', context)