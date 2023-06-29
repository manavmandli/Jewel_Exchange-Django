from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(WholesalerModel)
class WholesalerModelAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","role")

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id","category")

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=("id","product_name","product_category","available_qty","product_wgt","product_des","product_seller","product_purity","product_price","product_img1","created_at")

