from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Customer
from django.contrib import messages
from django.http import JsonResponse,HttpResponse

# Create your views here.

def show_account(request):
    return render(request,'account.html')

def user_register(request):    
    if request.method=='POST':  
        Name = request.POST.get('name')
        Username = request.POST.get('username')
        Email = request.POST.get('email')
        Address = request.POST.get('address')
        Mobile = request.POST.get('mobile')
        Password = request.POST.get('password')
        try:
            #create user object
            user = User.objects.create_user(
                username=Username,
                password=Password,
                email=Email
            )
            # create customer object
            customer = Customer.objects.create(
                user=user,
                name=Name,
                address = Address,
                phone=Mobile
            )
            customer.save()
            return JsonResponse({'message':'Registration Success'})
        except Exception as e:
            error_message = 'User already exist..!'
            return JsonResponse({'message':error_message},safe=False)

def user_login(request):
    if request.method=='POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return JsonResponse({'url':'account'})
        error_message = 'Invalid Username and Password..!'
        return JsonResponse({'message':error_message},safe=False)
    
def sign_out(request):
    logout(request)
    return redirect('index')