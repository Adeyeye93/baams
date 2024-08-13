from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageFilter, ImageEnhance
from multiselectfield import MultiSelectField


class Product(models.Model):
    MY_CHOICES = (
            ('Shoes', 'SHOES'),
            ('Athletic Shoes', 'Athletic Shoes'),
            ('Casual Shoes', 'Casual Shoes'),
            ('Formal Shoes', 'Formal Shoes'),
            ('Boots', 'Boots'),
            ('Sandals', 'Sandals'),
            ('Flip-Flops', 'Flip-Flops'),
            ('Loafers', 'Loafers'),
            ('Slip-Ons', 'Slip-Ons'),
            ('Sneakers', 'Sneakers'),
            ('Brogues', 'Brogues'),
            ('Running Shoes', 'Running Shoes'),
            ('Ballet Flats', 'Ballet Flats'),
            ('bags', 'BAGS')
              )
    name = models.CharField(max_length=150, null=True)
    price = models.FloatField()
    created_at =models.DateField(auto_now=False, auto_now_add=True)
    description = models.TextField(max_length=1000)
    weight = models.FloatField(null=True, blank=True, default=0.0)
    Availability = models.BooleanField(default=True, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    category = MultiSelectField(choices=MY_CHOICES, max_choices=3, max_length=100, default="category")
    

    def __str__(self):
        return self.name


    @property
    def get_image(self):
        return self.get_image_url()

    def get_image_url(self):
        if self.image:
            try:
                url = self.image.url
            except:
                url = ''
            return url
        return None
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date =models.DateField(auto_now=False, auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.IntegerField(null=True)

    def __str__(self):
        return f'ID:{self.transaction_id} ORDER_BY:{self.customer.username}'
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True, default=1)
    date_added =models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

        
class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    state = models.CharField(max_length=150, null=True)
    zipCode = models.CharField(max_length=150, null=True)
    date_added =models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.address)
    
