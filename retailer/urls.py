from django.contrib import admin
from django.urls import path,include
from  .import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('product',views.product,name="product"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('product_view/<int:id>',views.product_view,name="product_view"),
    path('remove-cart/<int:cart_id>', views.remove_cart, name="remove-cart"),
    path('plus-cart/<int:cart_id>', views.plus_cart, name="plus-cart"),
    path('minus-cart/<int:cart_id>', views.minus_cart, name="minus-cart"),
    path('cart', views.cart, name="cart"),
    path('like',views.like,name="like"),
    path('checkout',views.checkout,name="checkout"),
    path('order',views.order,name="order"),
    path('recent_order',views.recent_order,name="recent_order"),
]