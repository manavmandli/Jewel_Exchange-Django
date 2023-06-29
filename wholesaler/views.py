
from django.shortcuts import render,HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from jeweleryproject.urls import *
from wholesaler.models import *
from retailer.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
     if request.user.is_authenticated:
        findwholesaler=WholesalerModel.objects.get(email=request.user.email)
        context={
            'wholesaler':findwholesaler,
        }
        return render(request,"wholesaler/index.html",context)

@login_required
def services(request):
    if request.user.is_authenticated:
        findwholesaler=WholesalerModel.objects.get(email=request.user.email)
        context={
            'wholesaler':findwholesaler,
        }
        return render(request,"wholesaler/service.html",context)

@login_required
def contact(request):
    if request.user.is_authenticated:
        findwholesaler=WholesalerModel.objects.get(email=request.user.email)
        context={
            'wholesaler':findwholesaler,
        }
        return render(request,"wholesaler/contact.html",context)

@login_required
def product_management(request):
    if request.user.is_authenticated:
        findwholesaler=WholesalerModel.objects.get(email=request.user.email)
        find=WholesalerModel.objects.get(name=request.user)
        print("----",find.id)
        products=ProductModel.objects.all().filter(product_seller=find.id)
        print("request.user is:-",request.user.id)
        print("------",products)
        context={
            'product':products,
            'wholesaler':findwholesaler,
        }

        return render(request,"wholesaler/product.html",context)

@login_required
def add_product(request):
    if request.user.is_authenticated:
        success_message=None
        category=CategoryModel.objects.all()
        seller=WholesalerModel.objects.all()
        findwholesaler=WholesalerModel.objects.get(email=request.user.email)
        context={
        'category':category,
        'seller':seller,
        'wholesaler':findwholesaler.name
        }
        if request.method=='POST':
            product_name=request.POST['product_name']
            category=request.POST['product_categorie']
            product_category=CategoryModel.objects.get(category=category)
            product_qty=request.POST['available_quantity']
            product_weight=request.POST['product_weight']
            product_des=request.POST['product_description']
            seller=request.POST['seller']
            product_seller=WholesalerModel.objects.get(name=seller)
            product_purity=request.POST['product_purity']
            product_price=request.POST['product_price']
            main_image=request.FILES['img1']
            new_product=ProductModel.objects.create(product_name=product_name,product_category=product_category,available_qty= product_qty,product_wgt=product_weight,product_des=product_des,product_seller=product_seller,product_purity=product_purity,product_price=product_price,product_img1=main_image)
            new_product.save()
            success_message = 'Product Added Succesfully'
            return render(request,"wholesaler/product.html",{'success_message': success_message})
        return render(request,"wholesaler/add_products.html",context)
    
@login_required
def order_manage(request):
    user=request.user
    findwholesaler=WholesalerModel.objects.get(email=request.user.email)
    allorders=OrderModel.objects.filter(seller_name=findwholesaler.id)
    print("wholesaler all orders:-",allorders)
    context={
        'allorders':allorders,
        'findwholesaler':findwholesaler
    }
    return render(request,"wholesaler/order_manage.html",context)

@login_required
def order_update(request,pk):
    success_message=''
    if request.method =='POST':
        print("-----------------")
        orderdata=OrderModel.objects.get(id=pk)
        print("order data:",orderdata)
        orderdata.status=request.POST['status']
        # orderdata.date_delivery=request.POST['delivery_date']
        orderdata.save()
        success_message = 'Product Updated Succesfully'
        context = {
            "orderdata":orderdata,
        }
        return render(request,"wholesaler/order_manage.html",{'success_message': success_message}, context)
    return redirect('order_manage')

def order_detail(request,pk):
    user=request.user
    findwholesaler=WholesalerModel.objects.get(email=request.user.email)
    order=OrderModel.objects.get(id=pk)
    print("-------------- ALLORDERS : ",order.product_name)
    context={
        'allorders':[order],
        'findwholesaler':findwholesaler
    }
    return render(request,"wholesaler/order_details.html",context)
