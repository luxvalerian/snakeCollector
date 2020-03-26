from django.shortcuts import render
from django.http import HttpResponse

class Snake:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

snakes = [
  Snake('Shoelace', 'corn snake', 'wildtype orange and black', 2),
  Snake('Cotton Gin', 'western cottonmouth', 'dark, grayish-brown', 3),
  Snake('Wallflower', 'texas rat snake', 'tan olive-green blotchy', 1)
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello ---===e </h1>')

def about(request):
    return render(request, 'about.html')

def snakes_index(request):
    return render(request, 'snakes/index.html', { 'snakes': snakes })

