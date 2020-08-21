from django.shortcuts import render
import requests
import json
from .models import Input


# Create your views here.
def home(request):

  date = ""
  if request.method == "POST":
    date = str(request.POST.get('date'))

    input=Input()
    input.date = request.POST.get('date')
    input.save()


  api = requests.get("https://api.nasa.gov/planetary/apod?date="+date+"&api_key=Odhtl3AdNc2QxIiFSb6ZkjQoghsuoqLs7UvgLz0X").json()
  return render(request, 'home.html', {"api": api})


