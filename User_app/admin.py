from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(TestimonialsModel)
class TestimonialsModelAdmin(admin.ModelAdmin):
    list_display = ("id","user_id","organization_name","position","description")

@admin.register(SubscriberModel)
class SubscriberModelAdmin(admin.ModelAdmin):
    list_display = ("id","name","email")