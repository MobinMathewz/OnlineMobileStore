from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=128,unique=True)

    def __str__(self):
        return self.brand_name

class Mobile(models.Model):
    mobile_name = models.CharField(max_length=128,unique=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    ram = models.CharField(max_length=128)
    price = models.IntegerField()
    camera = models.CharField(max_length=128)
    os = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.mobile_name


class Orders(models.Model):
    personname = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    pin = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    email = models.CharField(max_length=180)
    productid = models.IntegerField()
    user = models.CharField(max_length=15)
    choice = (
        ('OrderRecieved','OrderRecieved'),
        ('Dispatched','Dispatched'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    status = models.CharField(max_length=250,choices=choice,default='OrderRecieved')
    active_status = models.IntegerField(default=1)
    def __str__(self):
        return self.personname