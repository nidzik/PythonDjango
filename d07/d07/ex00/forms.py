from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from ex00.models import Article

#class InscriptionForm(forms.Form):
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserSubmitForm(ModelForm):
    model = Article
#    username = forms.CharField(required = True)
#    password = forms.CharField(required = True, widget=forms.PasswordInput, initial='')
#    verif_password = forms.CharField(required = True, widget=forms.PasswordInput, initial='')
#    def clean(self):
#        form_data = super(InscriptionForm, self).clean() # appliquer la validation de la classe mere
#        u = User.objects.filter(username = form_data['username']) # recherche d'unicite
#        if len(u) > 0:
#            self._errors['username'] = ["Le nom saisi est déjà pris"]
#        if form_data['password'] != form_data['verif_password']:
#            self._errors['password'] = ["Le mot de passe doit être identique dans les 2 champs password"]
#        return form_data
