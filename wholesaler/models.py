from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class WholesalerModel(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=50)
    password=models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)
    
class CategoryModel(models.Model):
    category=models.CharField(max_length=200)

    def __str__(self):
        return str(self.category)
    
class ProductModel(models.Model):
    product_name=models.CharField(max_length=200)
    product_category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    available_qty=models.DecimalField(max_digits=3,decimal_places=0)
    product_wgt=models.PositiveIntegerField(null=True)
    product_des=models.TextField(verbose_name="Description")
    product_seller=models.ForeignKey(WholesalerModel,on_delete=models.CASCADE)
    product_purity=models.CharField(max_length=50)
    product_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    product_img1=models.ImageField(upload_to='products', blank=True, null=True, verbose_name="products")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    

    def __str__(self):
        return str(self.product_name)

