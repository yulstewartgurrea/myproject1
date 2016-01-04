from django import forms
from .models import MyUser
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active=True
        user.is_Customer=True
        if commit:
            user.save()
        return user