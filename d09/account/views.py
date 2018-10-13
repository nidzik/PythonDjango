from django.shortcuts import render
from django.http import Http404, HttpResponse
import json, random, sys
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView

class login1(FormView):
        form_class = AuthenticationForm
        template_name = "account/login.html"
        success_url = "/login"

def index(request):
    if request.is_ajax() == True:
        print ("REQUEST IS TRUE ")
        old_title = request.POST.get('element')
        titles = [
            '12345',
            '567',
            '890']
        new_title = random.choice(titles)
        data = json.dumps({
            'new': new_title,
            'old': old_title
            })
        return HttpResponse(data, content_type='application/json')
    else:
        
        return render(request, 'account/login.html')
        print("hooooo FALSE ")
        raise  Http404

    # Create your views here.
