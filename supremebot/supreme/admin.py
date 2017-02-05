from django.contrib import admin
from .models import upcoming_release, users
# Register your models here.

class upcoming_release_admin(admin.ModelAdmin):
    fieldsets =[
                (None, {'fields':['name']}),
                ('URL Information', {'fields':['url','image']}),
                ('Details', {'fields':['object_class', 'pub_date']})
               ]
class users_admin(admin.ModelAdmin):
    fieldsets = [
                ('Users Name', {'fields': ['first_name', 'last_name']}),
                ('Email',{'fields': ['email']}),
                ('Address',{'fields': ['address', 'shipping_address']}),
                ('Card Maker',{'fields': ['card_maker']}),
                ('Card Number', {'fields': ['credit_card_num']})
                ]
admin.site.register(upcoming_release, upcoming_release_admin)
admin.site.register(users, users_admin)
