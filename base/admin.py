from django.contrib import admin

from .models import User, InvestmentOption, InsuranceOption

admin.site.register(User)
admin.site.register(InvestmentOption)
admin.site.register(InsuranceOption)