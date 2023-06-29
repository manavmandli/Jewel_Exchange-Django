from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from verify_email.email_handler import send_verification_email
from django.contrib.auth.models import User
from retailer.models import *
from wholesaler.models import *
from django.contrib.auth.decorators import login_required
from retailer.views import *
from wholesaler.views import *
from User_app.models import *


def home(request):
    if request.method=="POST":
        name = request.POST['full-name']
        email = request.POST['email']
        subscriber = SubscriberModel(name=name, email=email)
        subscriber.save()
    product_detail = ProductModel.objects.all().order_by('-id')[:5]
    print(product_detail)
    testimonials=TestimonialsModel.objects.all().order_by('-id')[:5]
    print(testimonials)
    context={
        'collection':product_detail,
        'testimonial':testimonials,
    }
    return render(request,"jeweleryproject/index.html",context)

def products(request):
    return render(request,"jeweleryproject/productlist.html")

def services(request):
    return render(request,"jeweleryproject/services.html")

def contact(request):
    return render(request,"jeweleryproject/contact.html")

def login_view(request):
    success_message = None
    if request.user.is_authenticated:
        findwholesaler=WholesalerModel.objects.filter(email=request.user.email).exists()
        findretailor=RetailorModel.objects.filter(email=request.user.email).exists()
        if findwholesaler:
            # return render(request,"wholesaler/index.html")
            return redirect('wholesaler/home')
        elif findretailor:
            # return render(request,"retailor/index.html")
            return redirect('retailer/home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        print("retailor:-",user)
        if user is not None:
            login(request,user)
            findwholesaler=WholesalerModel.objects.filter(email=user.email).exists()
            findretailor=RetailorModel.objects.filter(email=user.email).exists()
            if findwholesaler:
                success_message = 'Login successful'
                return render(request,"wholesaler/index.html",{'success_message': success_message})
            elif findretailor:
                success_message = 'Login successful'
                return render(request,"retailor/index.html",{'success_message': success_message})
            else:
                error_message = 'User role is invalid'
                return render(request, 'jeweleryproject/login.html',{'error_message': error_message})
        else:
            error_message = 'Invalid username or password'
            return render(request, 'jeweleryproject/login.html',{'error_message': error_message})
    else:
        error_message = None
        return render(request, 'jeweleryproject/login.html',{'error_message': error_message})


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']
        password = request.POST['password']
        # Check if the username already exists
        if User.objects.filter(username=name).exists():
            error_message = 'Username already exists'
            return render(request, 'jeweleryproject/signup.html', {'error_message': error_message})
        
        user = User.objects.create_user(username=name, password=password, email=email)
        if role == 'wholesaler':
            wholesaler=WholesalerModel.objects.create(name=name,email=email,role=role,password=password)
            wholesaler.save()
        elif role == 'retailor':
            retailor=RetailorModel.objects.create(name=name,email=email,role=role,password=password)
            retailor.save()
        user.save()
        success_message = 'Registration Succesfully Completed'
        return render(request,'jeweleryproject/login.html',{'success_message': success_message})
        # return redirect('login')
    return render(request,"jeweleryproject/signup.html")


def logout_view(request):
    logout(request)
    return redirect('login')