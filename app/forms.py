from django import forms
from .models import MyUser, Category, Product
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

########################################################################################################
########################################################################################################
###################################     ADMIN FORMS       ##############################################

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

class ShopOwnerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(ShopOwnerRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active=True
        user.is_ShopOwner=True
        if commit:
            user.save()
        return user


class AddCategoryForm(forms.ModelForm):
    cname = forms.CharField(label="Category")
    class Meta:
        model = Category
        fields = ['cname']

class AddProductForm(forms.ModelForm):
    pname = forms.CharField(label="Product Name")
    cid = forms.ModelMultipleChoiceField(label="Category",widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    owner = forms.ModelChoiceField(label="Shop Owner",queryset=MyUser.object.filter(is_ShopOwner=True, is_active=True))
    class Meta:
        model = Product
        fields = ['pname', 'description', 'cid', 'owner']

########################################################################################################
########################################################################################################
###################################   SHOPOWNER FORMS     ##############################################

class SAddProductForm(forms.ModelForm):
    cid = forms.ModelMultipleChoiceField(label="Category",widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    pname = forms.CharField(label="Product Name")
    class Meta:
        model = Product
        fields = ['pname', 'description', 'cid']