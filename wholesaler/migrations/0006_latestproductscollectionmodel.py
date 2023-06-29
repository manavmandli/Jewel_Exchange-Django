# Generated by Django 3.2.3 on 2023-06-22 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wholesaler', '0005_alter_productmodel_product_wgt'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestProductsCollectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wholesaler.productmodel')),
            ],
        ),
    ]