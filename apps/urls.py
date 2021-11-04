from  django.urls import path
from . import  views

urlpatterns = [
    path('', views.firstpage),
    path('admin_login',views.admin_login),
    path('create_account',views.create_account),
    path('create_account2',views.create_account2),
    path('deposit',views.deposit),
    path('deposit_confirm',views.deposit_confirm),
    path('withdraw',views.withdraw),
    path('withdraw_confirm',views.withdraw_confirm),
    path('transaction_history',views.transaction_history1),
    path('profile',views.profile),
    path('home',views.home),

]