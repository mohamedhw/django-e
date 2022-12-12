from cProfile import label
from email.policy import default
from datetime import datetime
from itertools import product
from random import choices
from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django_countries.fields import CountryField

CATEGORY = [
    ('shirt', 'shirt'),
    ('sport', 'sport'),
    ('outwears', 'outwears')
]

LABEL = [
    ('NEW', 'new'),
    ('SALE', 'sale'),
]


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    info = models.TextField(null=True, blank= True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(default="default.png", upload_to='item_pic')
    category = models.CharField(choices=CATEGORY, max_length=8)
    label = models.CharField(choices=LABEL, max_length=7, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_add_to_cart_url(self):
        return reverse('store:add_to_cart', kwargs={'pk': self.pk})

    def get_shirt(self):
        return reverse("store:shirt")





class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.title

    def get_total_discount_price(self):
        return self.item.discount_price * self.quantity

    def get_total_price(self):
        return self.item.price * self.quantity

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_price()
        return self.get_total_price()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(default=datetime.now)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey("BillingAddress", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total



class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username