from django.contrib import admin

from .models import PizzaNames, PizzaCost, ExtraItemCost, ExtraSelected
# Register your models here.


admin.site.register(PizzaNames)
admin.site.register(PizzaCost)
admin.site.register(ExtraItemCost)
admin.site.register(ExtraSelected)
