from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User ,auth 
from .forms import *
from .models import *
import face_recognition
import cv2
import numpy as np
from django.http import JsonResponse
def login(request):
     if request.method =="POST":
        username=request.POST['uname']
        password=request.POST['pwd']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             if(user.is_superuser):
                  print(request.user.username)
                  return redirect('/register/')
             else:
               print(user.passenger.user_name)
               return redirect('/home')
             
        else:
             print(password)
             return render(request,'hai.html')
     
     return render(request,'login.html')
def account(request):
    return render(request,'myAcount.html')
#@login_required
def home(request):
     return render(request,'userHome.html')
def history(request):
     user=request.user
     prev_history=journey.objects.filter(user=user)
     # prev_history=journey.objects.filter(user_id=id)
     bal = user.passenger.balance
     
     context = {
           'history' : prev_history,
           'length':len(prev_history),
           'balance':bal
     }
     print(context['balance'])
     return render(request,'history.html',context)

def recharge(request):
        if request.method=="POST":
               user=request.user
               phone = request.POST['phone']
               password = request.POST['mobile']
               bala = request.POST['amount']
               bala = int(bala)
               amoun=bala
               bala = bala+user.passenger.balance
               if(user.passenger.password==password):
                   user.passenger.balance = bala                  
                   user.passenger.save()
                   return JsonResponse({'message':'Successfully recharged with ₹'+str(amoun)})
               return JsonResponse({'message':'Password Does not match please try again.'}) 
               # return JsonResponse({'message':'Password Doesn\'t match please try again.'})           

        return render(request,'rechargepafge.html')


    












