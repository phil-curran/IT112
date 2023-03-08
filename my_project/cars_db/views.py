from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Car

def cars(request):
    cars = Car.objects.all().values()
    template = loader.get_template('cars_db.html') 
    return render(request, 'cars_db.html', {'cars': cars})

def details(request, id):
    car = Car.objects.get(id=id)
    template = loader.get_template('details.html')
    return render(request, 'details.html', {'car': car})

