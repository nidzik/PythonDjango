from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('django', views.django, name='django'),
    url(r'^django/', views.django)
]
