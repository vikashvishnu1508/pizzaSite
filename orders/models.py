from django.db import models

# Create your models here.
#Pizza
class PizzaNames(models.Model):
    name                = models.CharField(max_length=250)
    
    def __str__(self):
        return f"Name : {self.name}"

class PizzaSize(models.Model):
    pizzaName           = models.ForeignKey(PizzaNames, on_delete=models.CASCADE, related_name='availableSizeOfPizza')
    size                = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Pizza : {self.pizzaName} and Size : {self.size}"

class PizzaSizeSelected(models.Model):
    pizzaName           = models.ForeignKey(PizzaNames, on_delete=models.CASCADE, related_name='selectedSizeOfPizza')
    selectedPizzaSize   = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Pizza : {self.pizzaName} and Size selected : {self.selectedPizzaSize}"

class PizzaCost(models.Model):
    pizzaName           = models.ForeignKey(PizzaNames, on_delete=models.CASCADE, related_name='myPizzaCost')
    pizzaSize           = models.ForeignKey(PizzaSize, on_delete=models.CASCADE, related_name='myPizzaSize')
    pizzaCost           = models.FloatField()
    
    def __str__(self):
        return f"Pizza : {self.pizzaName} ,Size : {self.pizzaSize} and Cost = {self.pizzaCost}"

#Toppings
class Toppings(models.Model):
    toppingName         = models.CharField(max_length=250)
    
    def __str__(self):
        return f"Topping : {self.toppingName}"
    
class ExtraSelected(models.Model):
    pizzaName           = models.ForeignKey(PizzaNames, on_delete=models.CASCADE, related_name='myPizzaExtraSelected')
    toppingsSelected    = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name='myToppingSelected')
    
    def __str__(self):
        return f"Pizza : {self.pizzaName} and Topping Selected : {self.toppingsSelected}"

class ExtraItemCost(models.Model):
    toppingName         = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name='myTopping')
    toppingCost         = models.FloatField()
    
    def __str__(self):
        return f"Topping : {self.toppingName} and Topping Cost : {self.toppingCost}"