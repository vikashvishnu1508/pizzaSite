from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import PizzaNames, PizzaSize, Toppings, PizzaCost
# Create your views here.
def index(request):
    context = {
        "pizzas" : PizzaNames.objects.all(),
        "pizzaSizes" : PizzaSize.objects.all(),
        "toppings" : Toppings.objects.all(),
        "cost" : "2"
    }
    #if (request.method == 'POST'):
        #myPizza = int(request.post['pizzaNameSelected'])
        #myPizzaSize = int(request.post['pizzaSizeSelected'])
        #topping = int(request.post['toppingSelected'])
        #pizzaCost = PizzaCost.objects.get(pizzaName=myPizza, pizzaSize=myPizzaSize)
        #PizzaCost.objects.get(pizzaName=1, pizzaSize=1)
        #context['cost'] = 120
        #return HttpResponseRedirect(reverse('orders'))
        #return render(request, 'orders/index.html', context)
    return render(request, 'orders/index.html', context)

def cost(request):
    context = {
        "cost" : "120"
    }
    if (request.method == 'POST'):
        context = {
        "cost" : "200"
        }
        return render(request, 'orders/cost.html', context)

    return render(request, 'orders/cost.html', context)