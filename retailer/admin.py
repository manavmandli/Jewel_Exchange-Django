from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(RetailorModel)
class RetailorModelAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","role")

@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ("id","buyer_name","product_name","product_quantity","product_category","product_wgt","product_price","total_price","product_img1")

@admin.register(ProductLikeModel)
class ProductLikeModelAdmin(admin.ModelAdmin):
    list_display = ("id","buyer_name","product_name","product_category","product_wgt","product_price","product_img1")

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ("id","buyer_name","seller_name","product_name","product_quantity","product_wgt","product_price","product_img1","shipping_agent","address","date_placed","status","date_delivery")


