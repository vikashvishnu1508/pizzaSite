from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import PizzaName, PizzaSize, PizzaCost, Toppings
#PizzaNames, PizzaSize, Toppings, PizzaCost

# Create your views here.
def index(request):
    context = {
        "pizzas"        : PizzaName.objects.all(),
        "pizzaSizes"    : PizzaSize.objects.all(),
        "toppings"      : Toppings.objects.all(),
    }
    # if (request.method == 'POST'):
    #     myPizza = int(request.POST['pizzaNameSelected'])
    #     topping = int(request.POST['toppingSelected'])
    #     return render(request, 'orders/index.html', context)
    return render(request, 'orders/index.html', context)

def cost(request):
    if (request.method == 'POST'):
        myPizza = int(request.POST['pizzaNameSelected'])
        myPizzaSize = int(request.POST['pizzaSizeSelected'])
        topping = int(request.POST['toppingSelected'])
        
        try:
            pizzaCost = PizzaCost.objects.get(pizzaName=myPizza, pizzaSize=myPizzaSize).pizzaCost
        except PizzaCost.DoesNotExist:
            pizzaCost = 'Not yet decided'
        try:
            toppingCost = Toppings.objects.get(pk=topping).toppingCost
        except PizzaCost.DoesNotExist:
            toppingCost = 'Not yet decided'
        
        context = {
            'pizzacost'     : pizzaCost,
            'toppingCost'   : toppingCost,
            'myPizza'       : myPizza,
            'myPizzaSize'   : myPizzaSize,
            'topping'       : topping
        }
        return render(request, 'orders/cost.html', context)
