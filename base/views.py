from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse

from .models import User, InvestmentOption, InsuranceOption, Transaction, TransactionExecuted, TransferOption, DepositOption, LoanOption
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
        try:

            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                login(request, user)
                return redirect('home')
            else:
                raise ValueError('Invalid form.')
            
        except ValueError as e:
            messages.error(request, e)

    return render(request, 'signup.html', {'form': form})

@login_required(login_url='login')
def depositPage(request):
    if request.method == 'POST':
        try:
            deposit_amount = request.POST['deposit_amount']
            deposit_method = request.POST['deposit_method']

            if deposit_amount == '':
                raise ValueError('Insert the values correctly.')
            
            deposit_amount = Decimal(deposit_amount)

            if(deposit_amount <= 0):
                raise ValueError('Only positive values accepted.')

            request.user.balance += deposit_amount
            request.user.score = min(10.00, deposit_amount/1000 + request.user.score)
            request.user.save()

            messages.error(request, 'Deposit succeded.')

            new_option = DepositOption(
                value=deposit_amount,
                method=deposit_method
            )
            new_option.save()

            new_transaction = Transaction(
                value=deposit_amount,
                user=request.user
            )
            new_transaction.save()

            execution = TransactionExecuted(
                transaction=new_transaction,
                option=new_option,
                quantity=1
            )
            execution.save()

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
            
            transfer_amount = Decimal(transfer_amount)

            destiny_user = get_object_or_404(User, CPF=destiny_cpf)

            if(Decimal(request.user.balance) < float(transfer_amount)):
                raise ValueError('Balance is less than value.')

            request.user.decrease_balance(transfer_amount)
            request.user.update_score(transfer_amount)
            request.user.save()
            
            destiny_user.add_balance(transfer_amount)
            destiny_user.save()
            
            messages.error(request, 'Tranfer succeded.')

            new_option = TransferOption(
                value=transfer_amount,
                destiny=destiny_user
            )
            new_option.save()

            new_transaction = Transaction(
                value=transfer_amount,
                user=request.user
            )
            new_transaction.save()

            execution = TransactionExecuted(
                transaction=new_transaction,
                option=new_option,
                quantity=1
            )
            execution.save()

            return redirect('home')
        
        except ValueError  as e:
            messages.error(request, e)
        except Http404:
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

            total_value = Decimal(quantity) * Decimal(option.value)

            if total_value > request.user.balance:
                raise ValueError('Balance is less than total value.')
            
            messages.success(request, 'Investment succed.')
            
            request.user.decrease_balance(total_value)
            request.user.save()

            option.decrease_quantity(quantity)
            option.save()

            new_transaction = Transaction(
                value=total_value,
                user=request.user
            )
            new_transaction.save()

            execution = TransactionExecuted(
                transaction=new_transaction,
                option=option,
                quantity=quantity
            )
            execution.save()

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
        options = options.filter(value__gte=min_price)
    if max_price:
        options = options.filter(value__lte=max_price)
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

            if(user.balance < option.value):
                raise ValueError('Balance is less than value.')

            if(user.score < option.min_score):
                raise ValueError('Minimum score was not reached.')

            user.decrease_balance(option.value)
            user.save()

            messages.success(request, 'Insurance succed')

            new_transaction = Transaction(
                value=option.value,
                user=request.user
            )
            new_transaction.save()

            execution = TransactionExecuted(
                transaction=new_transaction,
                option=option,
                quantity=1
            )
            execution.save()

            return redirect('home')
        
        except ValueError as e:
            messages.error(request, e)

    return render(request, 'insurance.html', context)

@login_required(login_url='login')
def historyPage(request):
    context = {
        'transactions': Transaction.objects.filter(user=request.user).prefetch_related('executed_option__option')
    }

    return render(request, 'history.html', context)

@login_required(login_url='login')
def loanPage(request):
        
    context = {
        'options': LoanOption.objects.all()
    }

    if request.method == 'POST':
        try:
            option_id = request.POST.get('option_id')

            loan_option = LoanOption.objects.get(id=option_id)
            user = request.user

            if(user.score < loan_option.min_score):
                raise ValueError('Minimum score was not reached.')

            user.add_balance(loan_option.value)
            user.save()

            messages.success(request, 'Loan succed')

            new_transaction = Transaction(
                value=loan_option.value,
                user=request.user
            )
            new_transaction.save()

            execution = TransactionExecuted(
                transaction=new_transaction,
                option=loan_option,
                quantity=1
            )
            execution.save()

            return redirect('home')

        except ValueError as e:
            messages.error(request, e)

    return render(request, 'loan.html', context)