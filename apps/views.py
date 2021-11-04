from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import account
from .models import transaction_history
from  datetime import datetime

def firstpage(request):

    return  render(request,"firstpage.html")


def admin_login(request):
    id=request.POST.get('id')
    pwd=request.POST.get('pwd')
    if(id=="admin" and pwd=="admin"):
        return  render(request,"homepage.html")
    else:
        messages.error(request,"Enter Correct Information ")
        return render(request,"firstpage.html")


def create_account(request):
    return render(request,"create_account.html")

def create_account2(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    email=request.POST.get('email')
    address=request.POST.get('address')
    number=request.POST.get('number')
    date=request.POST.get('date')
    item = account.objects.filter(id=id)
    if(len(item)==1):
        messages.error(request,"A Account Already exists with the ID number")
        return render(request,"create_account.html")
    else:

        account_details = account(id=id,name=name,email=email,address=address,number=number,date=date)
        account_details.save()
        messages.success(request, "Account is  created successfully")
        return render(request, "create_account.html")

def deposit(request):
    return render(request,"deposit.html")

def deposit_confirm(request):
    id=request.POST.get('id')
    if(id.isdecimal()==False):
        messages.error(request,"ID number must be a number")
        return render(request,"deposit.html")
    amount1=request.POST.get('amount')
    item=account.objects.filter(id=id)

    if(len(item)>=1 and amount1.isdecimal()):
        item2=account.objects.get(id=id)
        amount2 = int(amount1)
        if(amount2>=0):
           item2.balance+=amount2
           item2.save()
           nw=account.objects.get(id=id)
           now = datetime.now()


           dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
           transaction_details=transaction_history(id1=id,name=nw.name,transaction_type="Deposit",transaction_time=dt_string)
           transaction_details.save()
           messages.success(request,"Deposit is done successfully")
        else:
            messages.error(request,"Amount Should not be negative number")
        return render(request,"deposit.html")
    else:
        if(amount1.isdecimal()==False):
            messages.error(request,"Amount must be Digit or Positive number")
        if(len(item)==0):
            messages.error(request,"No such Account Number Available")
        return  render(request,"deposit.html")
def withdraw(request):
    return render(request,"withdraw.html")

def withdraw_confirm(request):
    id=request.POST.get('id')
    if(id.isdecimal()==False):
        messages.error(request,"ID number must be a number")
        return render(request,"deposit.html")
    amount1=request.POST.get('amount')
    item=account.objects.filter(id=id)

    if(len(item)>=1 and amount1.isdecimal()):
        item2=account.objects.get(id=id)
        amount2 = int(amount1)
        if(item2.balance-amount2>=0):
           item2.balance-=amount2
           item2.save()
           nw=account.objects.get(id=id)
           now = datetime.now()


           dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
           transaction_details=transaction_history(id1=id,name=nw.name,transaction_type="Withdraw",transaction_time=dt_string)
           transaction_details.save()
           messages.success(request,"Withdraw is done successfully")
        else:
            messages.error(request,"No sufficient balance available")
        return render(request,"withdraw.html")
    else:
        if(amount1.isdecimal()==False):
            messages.error(request,"Amount must be Digit or Positive number")
        if(len(item)==0):
            messages.error(request,"No such Account Number Available")
        return  render(request,"withdraw.html")


def transaction_history1(request):


        item=transaction_history.objects.all()
        return render(request,"transaction_history.html",{'c':item})


def profile(request):

    item=account.objects.all()
    return render(request,"profile.html",{'c':item})
def home(request):
    return render(request,"homepage.html")





