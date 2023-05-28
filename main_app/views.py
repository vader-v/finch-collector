from django.shortcuts import render

from django.http import HttpResponse

class Finch:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'tabby', 'Kinda rude.', 3),
  Finch('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Finch('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Finch('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def home(request):
  return HttpResponse('<h1>Hello tweet tweet </h1>')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })

def finch_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })