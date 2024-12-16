from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.registerPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('deposit/', views.depositPage, name='deposit'),
    path('transfer/', views.transferPage, name='transfer'),
    path('investment/', views.investmentPage, name='investment'),
    path('insurance/', views.insurancePage, name='insurance'),
]