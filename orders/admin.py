from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(PizzaNames)
admin.site.register(PizzaSize)
admin.site.register(PizzaSizeSelected)
admin.site.register(PizzaCost)
admin.site.register(Toppings)
admin.site.register(ExtraSelected)
admin.site.register(ExtraItemCost)