from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout 
from .forms import RegistrationForm, ShopOwnerRegistrationForm
from .models import MyUser, MyUserManager
# Create your views here.

def register_user(request):
	"""
	Register User
	"""
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_done')
        else:        
            form = RegistrationForm()

	return render(request, 'registration/register.html', {'form': form})

def register_done(request):
	return render(request, 'registration/register_done.html')


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

	return render(request, 'registration/login.html')

def logout_user(request):
	"""
	Logout View
	"""
	logout(request)
	return render(request, 'registration/logout.html')

def home(request):
	"""
	Redirects user by authority
	"""
	if request.user.is_authenticated():
		user = MyUser.object.get(pk=request.user.id)
		if user.is_admin:
			return redirect('admin_dashboard')
		if user.is_ShopOwner:
			return redirect('shopowner_dashboard')
		if user.is_Customer:
			return redirect('shop')

############################################################################
############################################################################
############################################################################

def admin_dashboard(request):
	if request.user.is_authenticated() and request.user.is_admin:
		admin = MyUser.object.get(pk=request.user.id)
		return render(request, 'admin/admin.html', {'admin': admin})
	else:
		return redirect('home')

def add_user(request):
	form = ShopOwnerRegistrationForm()
	user = MyUser.object.all()
	if request.method == 'POST' and request.user.is_admin:
		form = ShopOwnerRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('add_user')
	else:
		form = ShopOwnerRegistrationForm()
	return render(request, 'admin/adduser.html', {'form': form, 'user': user})


def add_category(request):
	if request.method =='POST' and request.user.is_admin:
		form = AddCategoryForm()
		if form.is_valid():
			form.save(commit=False)
			return redirect('add_category')
	elif request.user.is_admin:
		form = AddCategoryForm()
		category = Category.objects.all()
	return render(request, 'admin/category.html', {'form': form, 'category': category})

def delete_catagory(request, pk):
	if request.user.is_admin:
		category = Category.objects.get(pk=pk)
		category.is_active = False
		category.save()
		return redirect('add_category')
	else:
		return redirect('home')

def update_category(request, pk):
	category = get_object_404(Category, pk=pk)
	form = AddCategoryForm(request.POST or None, instance=category)
	if request.method == 'POST':
		category.cname = request.POST.get('cname')
		category.save()
		return redirect('add_category')

# def view_category(request):

############################################################################
############################################################################
############################################################################

def shopowner_dashboard(request):
	if request.user.is_authenticated() and request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		return render(request, 'shopowner/shopowner.html')
	else:
		return redirect('home')

############################################################################
############################################################################
############################################################################

def shop(request):
	if request.user.is_authenticated() and request.user.is_Customer:
		customer = MyUser.object.get(pk=request.user.id)
		return render(request, 'shop.html')
	else:
		return redirect('home')


