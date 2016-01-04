from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout 
from .forms import RegistrationForm
from .models import MyUser
# Create your views here.

def register_user(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_done')
        else:        
            form = RegistrationForm()

	return render(request, 'register.html', {'form': form})

def register_done(request):
	return render(request, 'register_done.html')


def login_user(request):
	"""
	Login View
	"""
	if request.method == 'POST':
		try:
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user is not None and user.is_active:
				login(request, user)
				return redirect('home')

		except MyUser.DoesNotExist:
			return redirect('login')

	elif request.user.is_authenticated():
		return redirect('home')

	return render(request, 'login.html')

def logout_user(request):
	"""
	Logout View
	"""
	logout(request)
	return render(request, 'logout.html')

def home(request):
	if request.user.is_authenticated():
		user = MyUser.object.get(pk=request.user.id)
		if user.is_admin:
			return redirect('admin_dashboard')
		if user.is_ShopOwner:
			return redirect('shopowner')
		if user.is_Customer:
			return redirect('customer')

############################################################################
############################################################################
############################################################################

def admin_dashboard(request):
	if request.user.is_authenticated() and request.user.is_admin:
		admin = MyUser.object.get(pk=request.user.id)
		return render(request, 'admin.html', {'admin': admin})
	else:
		return redirect('home')

############################################################################
############################################################################
############################################################################

def shopowner(request):
	if request.user.is_authenticated() and request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		return render(request, 'shopowner.html')
	else:
		return redirect('home')

############################################################################
############################################################################
############################################################################

def customer(request):
	if request.user.is_authenticated() and request.user.is_Customer:
		customer = MyUser.object.get(pk=request.user.id)
		return render(request, 'shop.html')
	else:
		return redirect('home')


