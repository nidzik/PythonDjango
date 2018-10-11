"""d07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from ex00.views import HomeRedirectView, ArticlesView, PublicationsView, ArticleDetailView, FavoritesView, RegisterView
urlpatterns = [
    url(r'^$', HomeRedirectView.as_view(), name='home'),
    url(r'^articles/$', ArticlesView.as_view(template_name = 'ex00/articles.html'), name="articles"),
    url(r'^login/$',  auth_views.LoginView.as_view(template_name='ex00/login.html'), name='login'),
    url(r'^admin/', admin.site.urls),

    url(r'^publications/$', PublicationsView.as_view(template_name = 'ex00/publications.html'), name='publications'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(template_name = "ex00/detail.html"), name="detail"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='ex00/logout.html'), name='logout'),
    url(r'^favorites/$', FavoritesView.as_view(template_name='ex00/favorites.html'), name="favorites"),
    url(r'^register/$', RegisterView.as_view(template_name='ex00/register.html'), name="register"),

]
