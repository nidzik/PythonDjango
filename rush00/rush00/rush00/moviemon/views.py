from django.shortcuts import render
from django.template import Context, Template
from django.template import loader
from django.http import HttpResponse


def index(request):
    t = loader.get_template('start_page.html')
    context = {
        'variable':'var',
        'gbimg':'gbcolor.jpg'
        }
    return HttpResponse(t.render(context, request))

def map(request):
    t= loader.get_template('map.html')
    context = {
        'gbimg':'map.png'
        }
    return HttpResponse(t.render(context, request))

# Create your views here.
