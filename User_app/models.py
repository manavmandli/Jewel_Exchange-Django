from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TestimonialsModel(models.Model):
    position = (
        ('Owner', 'Owner'),
        ('Employee', 'Employee'),
        ('Manager','Manager'),
    )
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    organization_name=models.CharField(max_length=100)
    position=models.CharField(max_length=50, choices=position, default='Owner')
    description=models.TextField(max_length=200)

    def __str__(self):
        return str(self.id)

class SubscriberModel(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()

    def __str__(self):
        return self.email