from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm

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

class AddGenderForm(forms.ModelForm):
    gender = forms.CharField(label="Gender")

    class Meta:
        model = Gender
        fields = ['gender']

class AddClassificationForm(forms.ModelForm):
    classname = forms.CharField(label="Classification")
    class Meta:
        model = Classification
        fields = ['classname']


class AddCategoryForm(forms.ModelForm):
    cname = forms.CharField(label="Category")
    class Meta:
        model = Category
        fields = ['cname']

class AddProductForm(forms.ModelForm):
    pname = forms.CharField(label="Product Name")
    cid = forms.ModelMultipleChoiceField(label="Category",widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    owner = forms.ModelChoiceField(label="Shop Owner",queryset=MyUser.object.filter(is_ShopOwner=True, is_active=True))
    sex = forms.ModelChoiceField(label="Gender", queryset=Gender.objects.all())
    class Meta:
        model = Product
        fields = ['pname', 'description', 'cid', 'owner', 'sex']

class ProfileForm(forms.ModelForm):
    fname = forms.CharField(label="First Name")
    lname = forms.CharField(label="Last Name")
    class Meta:
        model = UserProf
        fields = ['fname', 'lname']

    # def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     userprof = UserProf.objects.get(acct=MyUser, is_active=True)
    #     up = []
    #     for users in userprof:
    #         up.append((users.id, users.fname))
    #     self.fields['fname'] = forms.CharField(fname=up)

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['street', 'brgy', 'city', 'state', 'postalcode', 'pnum']

class PermanentAddressForm(forms.ModelForm):
    class Meta:
        model = PermanentAddress
        fields = ['street', 'brgy', 'city', 'state', 'postalcode', 'pnum']

########################################################################################################
########################################################################################################
###################################   SHOPOWNER FORMS     ##############################################

class SAddProductForm(forms.ModelForm):
    # cid = forms.ModelMultipleChoiceField(label="Category",widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    cid = forms.ModelChoiceField(label="Category", queryset=Category.objects.all())
    pname = forms.CharField(label="Product Name")
    sex = forms.ModelChoiceField(label="Gender", queryset=Gender.objects.all())
    # is_active = forms.BooleanField()
    class Meta:
        model = Product
        fields = ['pname', 'description', 'cid', 'sex']

class SImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['img1', 'img2', 'img3','img4', 'img5',]

########################################################################################################
########################################################################################################
###################################   CHANGE PASSWORD FORMS  ###########################################

class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Old Password"))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("New Password"))



