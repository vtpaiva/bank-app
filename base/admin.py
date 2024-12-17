from django.contrib import admin

from .models import User, InvestmentOption, InsuranceOption, Transaction, TransactionExecuted, TransactionOption, LoanOption, TransferOption, DepositOption

admin.site.register(User)
admin.site.register(InvestmentOption)
admin.site.register(InsuranceOption)
admin.site.register(Transaction)
admin.site.register(TransactionExecuted)
admin.site.register(TransactionOption)
admin.site.register(TransferOption)
admin.site.register(DepositOption)
admin.site.register(LoanOption)