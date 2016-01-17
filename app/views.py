from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout 
from .forms import *
from .models import *
from django.utils import timezone
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
#####################   ADMIN ADMIN ADMIN  #################################

def admin_dashboard(request):
	if request.user.is_authenticated() and request.user.is_admin:
		admin = MyUser.object.get(pk=request.user.id)
		return render(request, 'admin/admin.html', {'admin': admin})
	else:
		return redirect('home')

def add_user(request):
	form = ShopOwnerRegistrationForm()
	user = MyUser.object.filter(is_admin=True)
	user2 = MyUser.object.filter(is_ShopOwner=True)
	user3 = MyUser.object.filter(is_Customer=True)
	if request.method == 'POST' and request.user.is_admin:
		form = ShopOwnerRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('add_user')
	else:
		form = ShopOwnerRegistrationForm()
	return render(request, 'admin/adduser.html', {'form': form, 'user': user, 'user2':user2, 'user3':user3})


def add_category(request):
	if request.method =='POST' and request.user.is_admin:
		form = AddCategoryForm(request.POST)
		if form.is_valid():
			c = form.save(commit=False)
			c.save()
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

def add_product(request):
	if request.method == 'POST' and request.user.is_admin:
		form = AddProductForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('add_product')
	elif request.user.is_admin:
		form = AddProductForm()

	return render(request, 'admin/addproduct.html', {'form': form})

############################################################################
############################################################################
#####################SHOP OWNER SHOP OWNER##################################

def shopowner_dashboard(request):
	if request.user.is_authenticated() and request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		return render(request, 'shopowner/shopowner.html', {'shopowner': shopowner})
	else:
		return redirect('home')

def sview_category(request):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		category = Category.objects.all()
		return render(request, 'shopowner/viewcategory.html', {'shopowner': shopowner, 'category':category})

def sadd_product(request):
	form = SAddProductForm()
	cid = request.POST.get('cname')
	shopowner = MyUser.object.get(pk=request.user.id)
	sex = request.POST.get('gender')
	if request.method == 'POST' and request.user.is_ShopOwner:
		form = SAddProductForm(request.POST)
		if form.is_valid():
			frm = form.save(commit=False)
			shopowner = MyUser.object.get(pk=request.user.id)
			# gid = Gender.objects.get(pk=sex_id)
			# category = Category.objects.get(pk=cid_id)
			frm.owner = shopowner
			# frm.cid.add(category)
			frm.save()
			# p = Product(pname=request.POST.get('pname'), description=request.POST.get('description'), is_active=True,
			# 	owner=shopowner, dateadded=request.POST.get('dateadded'), cid=category)
			# p.save()
			return redirect('sadd_product')
		else:
			form = SAddProductForm(request.POST)

	return render(request, 'shopowner/addproduct.html',{'form':form, 'shopowner': shopowner})

def sview_product(request):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		product = Product.objects.filter(owner=shopowner, is_active=True)
		return render(request, 'shopowner/viewproduct.html', {'product': product, 'shopowner': shopowner})

def sview_productdetails(request, pk):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		product = get_object_or_404(Product, pk=pk)
		return render(request, 'shopowner/viewproductdetails.html', {'product':product, 'shopowner':shopowner})

def supdate_product(request, pk):
	if request.user.is_ShopOwner:
		cid = request.POST.get('cname')
		product = get_object_or_404(Product, pk=pk)
		form = AddProductForm(request.POST or None, instance=product )
		if request.method == 'POST':
			form = AddProductForm(request.POST)
			if form.is_valid:
				product.pname = request.POST.get('pname')
				product.description = request.POST.get('description')
				product.save()
				return redirect('/')

	return render(request, 'shopowner/updateproduct.html', {'form': form})

def delete_product(request, pk):
	if request.user.is_ShopOwner:
		product = get_object_or_404(Product, pk=pk)
		if request.method == 'POST':
			product.delete()
			return redirect('/')

	return render(request, 'shopowner/deleteproduct.html', {'product': product})

def sview_productbycategory(request, category_id):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		product = Product.objects.filter(cid=category_id, owner=shopowner)
		return render(request, 'shopowner/viewproductbycategory.html', {'product': product, 'shopowner': shopowner})


############################################################################
############################################################################
############################################################################

def shop(request):
	if request.user.is_authenticated() and request.user.is_Customer:
		customer = MyUser.object.get(pk=request.user.id)
		return render(request, 'shop.html')
	else:
		return redirect('home')


