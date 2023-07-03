from django.shortcuts import render,HttpResponse, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect
from retailer.models import *
from wholesaler.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from User_app.models import *

# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            name = request.POST['full-name']
            email = request.POST['email']
            subscriber = SubscriberModel(name=name, email=email)
            subscriber.save()
        product_detail = ProductModel.objects.all().order_by('-id')[:5]
        print(product_detail)
        testimonials=TestimonialsModel.objects.all().order_by('-id')[:5]
        print(testimonials)
        retailer=RetailorModel.objects.get(email=request.user.email)
        context={
            'retailer':retailer,
            'collection':product_detail,
            'testimonial':testimonials,
        }
    return render(request,"retailor/index.html",context)

@login_required
def product(request):
    if request.user.is_authenticated:
        retailer=RetailorModel.objects.get(email=request.user.email)
        category=CategoryModel.objects.all()
        product=ProductModel.objects.all()     
        context={
            'retailer':retailer,
            'category':category,
            'product':product,
        }
    return render(request,"retailor/product.html",context)

@login_required
def services(request):
    if request.user.is_authenticated:
        retailer=RetailorModel.objects.get(email=request.user.email)
        context={
            'retailer':retailer,
        }
    return render(request,"retailor/services.html",context)

@login_required
def contact(request):
    if request.user.is_authenticated:
        retailer=RetailorModel.objects.get(email=request.user.email)
        context={
            'retailer':retailer,
        }
        if request.method=="POST":
            name = request.POST['full-name']
            email = request.POST['email']
            subject=request.POST['subject']
            message=request.POST['message']
            subscriber = ContactFormModel(name=name, email=email,subject=subject,message=message)
            subscriber.save()
    return render(request,"retailor/contact.html",context)

@login_required
def product_view(request,id):
    if request.user.is_authenticated:
        product_id=id
        product_data=ProductModel.objects.all().filter(id=product_id)
        print("----",product_data)
        retailer=RetailorModel.objects.get(email=request.user.email)
        context={
            'retailer':retailer,
            'product':product_data,
        }
        if request.method=='POST':
                product=ProductModel.objects.get(id=product_id)
                item_already_in_cart = CartModel.objects.filter(product_name=product.product_name, buyer_name=request.user)
                if item_already_in_cart:
                    cp = get_object_or_404(CartModel, product_name=product.product_name, buyer_name=request.user)
                    cp.product_quantity += 1
                    cp.save()
                    return redirect('product')
                else:
                    new_cart=CartModel.objects.create(buyer_name=request.user.username,product_name=product.product_name,product_category=product.product_category.category,product_wgt=product.product_wgt,product_price=product.product_price,product_img1=product.product_img1)
                    new_cart.save()
                    success_message = 'Product Added into Your Cart'
                    # return render(request,"retailor/product.html",{'success_message': success_message})
                    return redirect('product')

            # elif request.action=='/retailer/product_view':
            #     product=ProductModel.objects.get(id=product_id)
            #     print("-----123",product.product_name)
            #     new_cart=ProductLikeModel.objects.create(user_name=request.user.username,product_name=product.product_name,product_category=product.product_category.category,product_wgt=product.product_wgt,product_price=product.product_price,product_img1=product.product_img1)
            #     new_cart.save()
            #     success_message = 'Product Added into your wishlist'
            #     return render(request,"retailor/product_view.html",{'success_message': success_message})
    return render(request,"retailor/product_view.html",context)

@login_required
def like(request):
    return render(request,"retailor/like.html")


@login_required
def cart(request):
    if request.user.is_authenticated:
        retailer=RetailorModel.objects.get(email=request.user.email)
        cart_data=CartModel.objects.all().filter(buyer_name=request.user)
        item=0
        total_price = 0 
        for i in cart_data:
            item =item+1
            try:
                cp = get_object_or_404(CartModel, id=i.id)
                cp.total_price=cp.product_price*cp.product_quantity
                cp.save()
                total_price=total_price+cp.total_price
            except CartModel.DoesNotExist:
                print("CartModel object does not exist for id:", i.id)
        context={
            'retailer':retailer,
            'cart_items':cart_data,
            'items':item,
            'totalamt':total_price
        }
    return render(request,"retailor/cart.html",context)

@login_required
def minus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(CartModel, id=cart_id)
        # Remove the Product if the quantity is already 1
        if cp.product_quantity == 1:
            cp.delete()
        else:
            cp.product_quantity -= 1
            cp.save()
    return redirect('cart')

@login_required
def remove_cart(request, cart_id):
    if request.method == 'GET':
        c = get_object_or_404(CartModel, id=cart_id)
        c.delete()
    return redirect('cart')

@login_required
def plus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(CartModel, id=cart_id)
        cp.product_quantity += 1
       
        cp.save()
    return redirect('cart')

@login_required
def checkout(request):
    user=request.user
    retailer=RetailorModel.objects.get(email=request.user.email)
    cart_data=CartModel.objects.all().filter(buyer_name=request.user)
    item=0
    total_price = 0 
    shipping_total= 0
    for i in cart_data:
            item =item+1
            try:
                cp = get_object_or_404(CartModel, id=i.id)
                cp.total_price=cp.product_price*cp.product_quantity
                cp.save()
                total_price=total_price+cp.total_price
                shipping_total=total_price+500
            except CartModel.DoesNotExist:
                print("CartModel object does not exist for id:", i.id)
    context={
            'retailer':retailer,
            'cart_items':cart_data,
            'items':item,
            'totalamt':total_price,
            'shipping_total':shipping_total
        }
    return render(request,"retailor/checkout.html",context)

@login_required
def order(request):
    user=request.user
    success_message=''
    cart_data=CartModel.objects.all().filter(buyer_name=request.user)
    if request.method=="POST":
        shipping_agent="Fedex Delivery | Delivery: 2-4 Days"
        buyer_name=request.user.username
        address=request.POST['billing-address']
        state=request.POST['billing-state']
        zip=request.POST['billing-zip']
        billing_address=address+ state+ str(zip)
        for i in cart_data:
            find_product = ProductModel.objects.filter(product_name=i.product_name).first()
            print("find_product:---",find_product)
            print("seller name :-",find_product.product_seller)
            new_order=OrderModel.objects.create(product_name=i.product_name,seller_name=find_product.product_seller,buyer_name=buyer_name,product_quantity=i.product_quantity,product_wgt=i.product_wgt,product_price=i.product_price,total_price=i.total_price,product_img1=i.product_img1,shipping_agent=shipping_agent,address=billing_address)
            i.delete()
            new_order.save()
            success_message = 'Payment Successfully Paid'
    return render(request,"retailor/order.html",{'success_message': success_message})

@login_required
def recent_order(request):
    user=request.user
    retailer=RetailorModel.objects.get(email=request.user.email)
    print("user:-",user)
    recent_order=OrderModel.objects.all().filter(buyer_name=user)
    print("orders:-",recent_order)
    context={
        'orders':recent_order,
        'retailer':retailer
    }
    return render(request,"retailor/order.html",context)


