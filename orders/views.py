from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import PizzaNames, PizzaSize, Toppings, PizzaCost
context = {
        "pizzas" : PizzaNames.objects.all(),
        "pizzaSizes" : PizzaSize.objects.all(),
        "toppings" : Toppings.objects.all(),
        "cost" : "2"
    }
# Create your views here.
def index(request):
    
    if (request.method == 'POST'):
        myPizza = int(request.POST['pizzaNameSelected'])
        myPizzaSize = int(request.POST['pizzaSizeSelected'])
        topping = int(request.POST['toppingSelected'])
        pizzaCost = PizzaCost.objects.get(pizzaName=myPizza, pizzaSize=myPizzaSize)
        #PizzaCost.objects.get(pizzaName=1, pizzaSize=1)
        context['cost'] = pizzaCost.pizzaCost
        
        return render(request, 'orders/index.html', context)
    return render(request, 'orders/index.html', context)

def cost(request):
    context['cost'] = 120
    if (request.method == 'POST'):
        context['cost'] = 200
        return render(request, 'orders/cost.html', context)

    return render(request, 'orders/cost.html', context)