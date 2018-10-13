"""d09 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from account.views import login1
urlpatterns = [
     path('', views.index, name='index'),
    url( r'^login1/$', login1.as_view(template_name='account/login.html'), name='login1'),
    path('admin/', admin.site.urls),
     url(r'^login/$', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    
]
