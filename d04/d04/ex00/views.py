from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def index(request):
    return render(request, 'ex00/index.html')

# Create your views here.
