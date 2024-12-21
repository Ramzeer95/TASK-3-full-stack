from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def hello_world_template(request):
    return render(request, 'hello_world.html')
