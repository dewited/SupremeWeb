from __future__ import unicode_literals

from django.db import models

# Create your models here.

class users(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    credit_card_num = models.IntegerField()
    shipping_address = models.CharField(max_length = 200)
    card_maker = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    def __str__(self):
        total = self.first_name + " " + self.last_name
        return total

class upcoming_release(models.Model):
    name = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)
    object_class = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date_published')
    def __str__(self):
        return self.name
