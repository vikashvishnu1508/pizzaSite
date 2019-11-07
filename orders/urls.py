from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cost/", views.cost, name="cost")
]
