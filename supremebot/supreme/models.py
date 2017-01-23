from __future__ import unicode_literals

from django.db import models

# Create your models here.

class users(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    credit_card_num = models.IntegerField(max_length = 200)
    shipping_address = models.CharField(max_length = 200)
    card_maker = models.CharField(max_length = 200)

class upcoming_release(models.Model):
    name = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)


