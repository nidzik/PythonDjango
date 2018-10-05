from django.shortcuts import render
from django.template import Context, Template
from django.template import loader
from django.http import HttpResponse
from django.template.loader import render_to_string

def index(request):
    return render(request, 'ex01/base.html')

def django(request):
    t = loader.get_template('base.html')
#    c = Context({"variable": "opvar"})
    context = {
        'variable':'var',
        }
    return HttpResponse(t.render(context, request))
# Create your views here.
