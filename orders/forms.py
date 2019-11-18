from django import forms

from .models import *

class PizzaNameForm(forms.ModelForm):
    class Meta:
        model = PizzaName
        fields = [
            'name'
        ]

class PizzaSizeForm(forms.ModelForm):
    class Meta:
        model = PizzaSize
        fields = [
            'size'
        ]

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Toppings
        fields = [
            'toppingName'
        ]



class PizzaNameForm1(forms.Form):
    name = forms.ModelChoiceField(queryset= PizzaName.objects.values('name'), required=True,flat=True)

class PizzaSizeForm1(forms.Form):
    size = forms.ModelChoiceField(queryset=PizzaSize.objects.values_list('size'), required=True)

class ToppingForm1(forms.Form):
    toppigName = forms.ModelChoiceField(queryset=Toppings.objects.values_list('toppingName'),required=True)