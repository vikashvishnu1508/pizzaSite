from django.db import models

# Create your models here.
class PizzaNames(models.Model):
    name = models.CharField(max_length=250)

class PizzaCost(models.Model):
    pizzaName           = models.ForeignKey(PizzaNames, on_delete=models.CASCADE, related_name='myPizzaCost')
    smallPizzaCost      = models.FloatField()
    mediiumPizzaCost    = models.FloatField()
    largePizzaCost      = models.FloatField()
    
    def __str__(self):
        return f""" my pizza is = {self.pizzaName}. Its cost is as belowI
                    \n  small = {self.smallPizzaCost}
                    \n  medium = {self.mediiumPizzaCost}
                    \n  large = {self.largePizzaCost}"""

class ExtraItemCost(models.Model):
    extraCheeseCost             = models.FloatField()
    onionToppingCost            = models.FloatField()
    grilledMushroomToppingCost  = models.FloatField()
    jalapenoToppingCost         = models.FloatField()
    blackOliveToppingCost       = models.FloatField()
    chickenToppingCost          = models.FloatField()
    bbqChickenToppingCost       = models.FloatField()

class ExtraSelected(models.Model):
    pizzaName                   = models.ForeignKey(PizzaNames, on_delete=models.CASCADE, related_name='myPizzaExtra')
    isExtraCheese               = models.BooleanField()
    isOnionTopping              = models.BooleanField()
    isGrilledMushroomTopping    = models.BooleanField()
    isJalapenoTopping           = models.BooleanField()
    isBlackOliveTopping         = models.BooleanField()
    isChickenTopping            = models.BooleanField()
    isBbqChickenTopping         = models.BooleanField()
    
    def __str__(self):
        return f"""my pizza is = {self.pizzaName}. I have selected the below
                    \n  extraCheese              =  {self.isExtraCheese}
                    \n  onionTopping             =  {self.isOnionTopping}
                    \n  grilledMushroomTopping   =  {self.isGrilledMushroomTopping}
                    \n  jalapenoTopping          =  {self.isJalapenoTopping}
                    \n  blackOliveTopping        =  {self.isBlackOliveTopping}
                    \n  chickenTopping           =  {self.isChickenTopping}
                    \n  bbqChickenTopping        =  {self.isBbqChickenTopping}
                    End
                """