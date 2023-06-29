from django.db import models
from wholesaler.models import WholesalerModel
from django.utils import timezone
from datetime import datetime
import datetime

# Create your models here.
class RetailorModel(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=50)
    password=models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)
    
class CartModel(models.Model):
    buyer_name=models.CharField(max_length=200,default="")
    product_name=models.CharField(max_length=200)
    product_quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    product_category=models.CharField(max_length=200)
    product_wgt=models.PositiveIntegerField(null=True)
    product_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    product_img1=models.ImageField(upload_to='products/cart/', blank=True, null=True, verbose_name="products")

    def __str__(self):
        return str(self.id)

class ProductLikeModel(models.Model):
    buyer_name=models.CharField(max_length=200,default="")
    product_name=models.CharField(max_length=200)
    product_category=models.CharField(max_length=200)
    product_wgt=models.PositiveIntegerField(null=True)
    product_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    product_img1=models.ImageField(upload_to='products/cart', blank=True, null=True, verbose_name="products")

    def __str__(self):
        return str(self.id)
    
class OrderModel(models.Model):
    STATUS_CHOICES = [
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('processing', 'Processing'),
        ('pending',   'Pending')
    ]
    def get_future_date():
        current_datetime = datetime.datetime.now()
        future_datetime = current_datetime + datetime.timedelta(days=7)
        future_datetime = future_datetime
        utcoffset = future_datetime.utcoffset()
        return future_datetime
    
    product_name=models.CharField(max_length=200)
    buyer_name=models.CharField(max_length=200,default="")
    seller_name=models.ForeignKey(WholesalerModel,on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    product_wgt=models.PositiveIntegerField(null=True)
    product_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    product_img1=models.ImageField(upload_to='products/cart/', blank=True, null=True, verbose_name="products")
    shipping_agent=models.CharField(max_length=200,default="")
    address=models.CharField(default="",max_length=500)
    date_placed = models.DateTimeField(default=timezone.now)
    date_delivery = models.DateTimeField(default=get_future_date)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return str(self.id)
    

    