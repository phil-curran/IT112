from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
  template = loader.get_template('base.html')
  name = request.GET.get("user_name", "Stranger") 
  return render(request, 'base.html', {'name': name})