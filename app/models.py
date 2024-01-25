from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField

class Textile(models.Model):
    textile = models.CharField(max_length=50)
    
    def __str__(self):
        return self.textile    
    
class Color(models.Model):
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return self.color

class Size(models.Model):
    size = models.IntegerField()
    
    def __str__(self):
        return self.size

def image_path(instance, filename):    
    directory = instance.name
    return f'images/dresses/{directory}/{filename}'

class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.IntegerField()    
    image = ThumbnailerImageField(upload_to=image_path)    
    description = models.TextField(max_length=1000)
    textile = models.ForeignKey(Textile, related_name='products', on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.name
    
def image_path_for_add_images(instance, filename):
    directory = instance.product.name    
    return f'images/dresses/{directory}/{filename}'

class AdditionalImage(models.Model):
    product = models.ForeignKey(Product, related_name='additional_images', on_delete=models.CASCADE)
    additional_image = ThumbnailerImageField(upload_to=image_path_for_add_images)
    
class Stock(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name='stocks_product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    color = models.ForeignKey(Color, related_name='stock', on_delete=models.CASCADE)
    size = models.CharField(max_length=30)
    
    def __str__(self):
        return self.product
    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    order_quantity = models.IntegerField()
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    clients = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    price = models.IntegerField()
    subtotal = models.IntegerField()

class BoughtProduct(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    clients = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    products = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    price = models.IntegerField()
    subtotal = models.IntegerField()
    


