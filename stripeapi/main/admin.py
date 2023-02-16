from django.contrib import admin

from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


admin.site.register(Item, ItemAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('total_price', 'discount', 'tax')


admin.site.register(Order, OrderAdmin)
admin.site.register(Discount)
admin.site.register(Tax)
