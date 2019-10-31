from django.http import HttpResponse
from django.shortcuts import render

from .models import PizzaNames
# Create your views here.
def index(request):
    context = {
        "pizzas" : PizzaNames.objects.all(),
        "pizzasCount" : PizzaNames.objects.all().count()
    }
    return render(request, 'orders/index.html', context)
    #return HttpResponse("Project 3: TODO")
