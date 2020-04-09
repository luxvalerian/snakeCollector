from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Snake, Toy
from .forms import FeedingForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def snakes_index(request):
    snakes = Snake.objects.all()
    return render(request, 'snakes/index.html', { 'snakes': snakes })

def snakes_detail(request, snake_id):
    snake = Snake.objects.get(id=snake_id)
    toys_snake_doesnt_have = Toys.objects.exclude(id__in = snake.toys.all().values_list('id'))
    feeding_form = FeedingForm()

    return render(request, 'snakes/detail.html', { 
        'snake': snake,
        'feeding_form': feeding_form,
        'toys': toys_snake_doesnt_have 
        
        })

def add_feeding(request, snake_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.snake_id = snake_id
    new_feeding.save()
  return redirect('detail', snake_id=snake_id)

def assoc_toy(request, snake_id, toy_id):
    Snake.objects.get(id=snake_id).toys.add(toy_id)
    return redirect('detail', snake_id=snake_id)
    
class SnakeCreate(CreateView):
    model = Snake
    fields = '__all__'

class SnakeUpdate(UpdateView):
    model = Snake
    fields = ['breed', 'description', 'age']

class SnakeDelete(DeleteView):
    model = Snake
    success_url = '/snakes/'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']
    success_url = '/toys/'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']
    success_url = '/toys/'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'