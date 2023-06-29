# Generated by Django 4.1.7 on 2023-05-24 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wholesaler', '0005_alter_productmodel_product_wgt'),
        ('retailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='product_img1',
            field=models.ImageField(blank=True, null=True, upload_to='products/cart/', verbose_name='products'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='product_wgt',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='seller_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wholesaler.wholesalermodel'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='product_name',
            field=models.CharField(max_length=200),
        ),
    ]