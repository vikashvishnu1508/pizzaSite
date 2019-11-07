from django.db import models

# Create your models here.

class PizzaName(models.Model):
    name                = models.CharField(max_length=250, default=None, null=False)

    def __str__(self):
        return f"Name : {self.name}"

class PizzaSize(models.Model):
    size                = models.CharField(max_length=100, default=None, null=False)

    def __str__(self):
        return f"Size : {self.size}"

class PizzaCost(models.Model):
    pizzaName           = models.ForeignKey(PizzaName, on_delete=models.CASCADE)
    pizzaSize           = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    pizzaCost           = models.FloatField(default=None, null=False)

    def __str__(self):
        return f"Pizza : {self.pizzaName} ,Size : {self.pizzaSize} and Cost = {self.pizzaCost}"



class Toppings(models.Model):
    toppingName         = models.CharField(max_length=250, default=None, null=False)
    toppingCost         = models.FloatField(default=None, null=False)

    def __str__(self):
        return f"Topping : {self.toppingName} and Topping Cost : {self.toppingCost}"












# class ToppingsSelected(models.Model):
#     pizzaName           = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='selectedPizzaToppings')
#     selectedToppings    = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Pizza : {self.pizzaName} and Topping Selected : {self.toppingsSelected}"

# class PizzaSelected(models.Model):
#     pizzaName           = models.ForeignKey(PizzaName, on_delete=models.CASCADE)
#     selectedPizza       = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Pizza : {self.pizzaName} and Size selected : {self.selectedPizzaSize}"
