from django.contrib import admin
from django.urls import path,include
from  .import views
from jeweleryproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home,name="home"),
    path('product_management',views.product_management,name="product_management"),
    path('add_product',views.add_product,name="add_product"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('order_manage/',views.order_manage,name="order_manage"),
    path('order_update/<int:pk>/',views.order_update,name="order_update"),
    path('order_detail/<int:pk>/',views.order_detail,name="order_detail"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)