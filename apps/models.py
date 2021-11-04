


from django.db import models
class account(models.Model):
    id=models.IntegerField(blank=False,primary_key=True)
    name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50,blank=False)
    address=models.CharField(max_length=50,blank=False)
    number=models.CharField(max_length=50,blank=False)
    date=models.CharField(max_length=50,blank=False)
    balance=models.IntegerField(blank=False,default=0)

class transaction_history(models.Model):
    id1=models.IntegerField(blank=False)
    name=models.CharField(blank=False,max_length=50)
    transaction_type=models.CharField(blank=False,max_length=50)
    transaction_time=models.CharField(blank=False,max_length=50)