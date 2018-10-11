from django.shortcuts import render
from ex00.models import Article, UserFavouriteArticle
from django.views.generic import ListView, FormView, DetailView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from .forms import UserCreateForm
from django.contrib.auth.models import User


#class home(RedirectView):
#         pattern_name = '/articles'

#class login(FormView):
#        form_class = AuthenticationForm
#        template_name = "ex00/login.html"
#        success_url = "/articles"

class ArticlesView(ListView):
        model = Article
        template_name = "ex00/articles.html"

class HomeRedirectView(RedirectView):
    """
    simple redirection vers articles
    """
    permanent = False
    query_string = True
    pattern_name = 'articles'
    #pattern_name = redirect(reverse('articles'))

    def get_redirect_url(self, *args, **kwargs):

        return super(HomeRedirectView, self).get_redirect_url(*args, **kwargs)
    
class PublicationsView(ListView):
	model = Article

class ArticleDetailView(DetailView):
	model = Article

class FavoritesView(ListView):
	model = UserFavouriteArticle

class RegisterView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = "/"
# Create your views here.
