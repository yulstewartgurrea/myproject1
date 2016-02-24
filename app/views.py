from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout 
from .forms import *
from .models import *
from django.utils import timezone
from django.contrib.auth.forms import SetPasswordForm
from django.core.urlresolvers import reverse
from django.db.models import Sum, Avg
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
            form = RegistrationForm(request.POST)

	return render(request, 'registration/register.html', {'form': form})

def register_done(request):
	return render(request, 'registration/registerdone.html')


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

			else:
				return redirect('login_error')

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

def login_error(request):
	return render(request, 'registration/login_error.html')

#####################   ADMIN ADMIN ADMIN  #################################
#####################   ADMIN ADMIN ADMIN  #################################
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

#####################SHOP OWNER SHOP OWNER##################################
#####################SHOP OWNER SHOP OWNER##################################
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
	form2 = SImageForm()
	shopowner = MyUser.object.get(pk=request.user.id)
	if request.method == 'POST' and request.user.is_ShopOwner:
		form = SAddProductForm(request.POST)
		form2 = SImageForm(request.POST, request.FILES)
		if form.is_valid() and form2.is_valid():
			shopowner = MyUser.object.get(pk=request.user.id)
			# pid = Product.objects.get(owner=shopowner, is_active=True)
			frm = form.save(commit=False)
			image = form2.save()
			frm.owner = shopowner
			frm.is_active=True
			frm.save()
			# image.pid = pid
			image.save()
			pid = Product.objects.get(id=frm.pk)
			image.pid = pid
			image.save()
			return redirect('sadd_product')
		else:
			form = SAddProductForm(request.POST)
			form2 = SImageForm(request.POST)

	return render(request, 'shopowner/addproduct.html',{'form':form, 'shopowner': shopowner, 'form2': form2})

def sview_product(request):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		# prid = Product.objects.get()
		product = Product.objects.filter(owner=shopowner, is_active=True)
		return render(request, 'shopowner/viewproduct.html', {'product': product, 'shopowner': shopowner})

def sview_productdetails(request, pk):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		product = get_object_or_404(Product, pk=pk)
		image = get_object_or_404(Image, pid=pk)
		return render(request, 'shopowner/viewproductdetails.html', {'product':product, 'shopowner':shopowner, 'image': image})

def supdate_product(request, pk):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		product = get_object_or_404(Product, pk=pk)
		image = get_object_or_404(Image, pid=pk)
		form = SAddProductForm(request.POST or None, instance=product)
		form2 = SImageForm(request.POST or None, request.FILES, instance=image)
		if request.method == 'POST':
			form = SAddProductForm(request.POST, instance=product)
			form2 = SImageForm(request.POST, request.FILES, instance=image)
			if form.is_valid() and form2.is_valid():
				shopowner = MyUser.object.get(pk=request.user.id)
				frm = form.save(commit=False)
				image = form2.save(commit=False)
				frm.owner = shopowner
				frm.save()
				image.save()
				pid = Product.objects.get(id=frm.pk)
				image.pid = pid
				image.save()
				return redirect('sview_product')

	return render(request, 'shopowner/updateproduct.html', {'form': form, 'product': product, 'shopowner': shopowner, 'form2': form2})

def sdelete_product(request, pk):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		product = get_object_or_404(Product, pk=pk)
		if request.method == 'POST':
			product.delete()
			return redirect('sview_product')

	return render(request, 'shopowner/deleteproduct.html', {'product': product, 'shopowner': shopowner})

def sview_productbycategory(request, category_id):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		product = Product.objects.filter(cid=category_id, owner=shopowner)
		return render(request, 'shopowner/viewproductbycategory.html', {'product': product, 'shopowner': shopowner})

def ssettings(request):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		userprof = UserProf.objects.filter(acct=shopowner, is_active=True)
		add1 = BillingAddress.objects.filter(acct=shopowner, is_active=True)
		add2 = PermanentAddress.objects.filter(acct=shopowner, is_active=True)
		shopname = Shop.objects.filter(sid=shopowner, is_active=True)
	return render(request, 'shopowner/settings.html', {'shopowner': shopowner, 'userprof':userprof, 'add1':add1, 'add2':add2, 'shopname': shopname}) 

def ssupdate_profile(request):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		form = ProfileForm(instance=request.user.profile)
		if request.method == 'POST':
			form = ProfileForm(request.POST, instance=request.user.profile)
			if form.is_valid():
				shopowner = MyUser.object.get(pk=request.user.id)
				frm = form.save(commit=False)
				frm.acct = shopowner
				frm.save()
			return redirect('ssettings')
		return render(request, 'shopowner/up.html', {'shopowner': shopowner, 'form':form})

def ssupdate_billingaddress(request):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		form = BillingAddressForm(instance=request.user.profile1)
		if request.method == 'POST':
			form = BillingAddressForm(request.POST, instance=request.user.profile1)
			if form.is_valid():
				frm = form.save(commit=False)
				shopowner = MyUser.object.get(pk=request.user.id)
				frm.acct = shopowner 
				frm.save()
			return redirect('ssettings')
	return render(request, 'shopowner/ba.html', {'shopowner': shopowner, 'form':form})

def ssupdate_permanentaddress(request):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		form = PermanentAddressForm(instance=request.user.profile2)
		if request.method == 'POST':
			form = PermanentAddressForm(request.POST, instance=request.user.profile2)
			if form.is_valid():
				frm = form.save(commit=False)
				shopowner = MyUser.object.get(pk=request.user.id)
				frm.acct = shopowner
				frm.save()
				return redirect('ssettings')
	return render(request, 'shopowner/pa.html', {'shopowner': shopowner, 'form':form})

def shopname(request):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		form = ShopForm(instance=request.user.profile3)
		if request.method == 'POST':
			form = ShopForm(request.POST, instance=request.user.profile3)
			if form.is_valid():
				frm = form.save(commit=False)
				shopowner = MyUser.object.get(pk=request.user.id)
				frm.acct = shopowner
				frm.save()
				return redirect('ssettings')
	return render(request, 'shopowner/pa.html', {'shopowner': shopowner, 'form':form})

def sorder(request):
	if request.user.is_ShopOwner:
		shopowner = MyUser.object.get(pk=request.user.id)
		sname = Shop.objects.get(sid=shopowner)
		cart = Cart.objects.filter(shop=sname)
		product = Product.objects.filter(is_active=True)


	return render(request, 'shopowner/sorder.html', {'shopowner': shopowner, 'product': product, 'cart': cart})
########################    CUSTOMERS PAGE   ###############################
########################    CUSTOMERS PAGE   ###############################
########################    CUSTOMERS PAGE   ###############################

def shop(request):
	if request.user.is_authenticated() and request.user.is_Customer:
		customer = MyUser.object.get(pk=request.user.id)
		return render(request, 'homepage.html')
	else:
		return redirect('home')

def allproducts(request):
	if request.user.is_Customer:
		c = Product.objects.filter(is_active=True).count()
		customer = MyUser.object.get(pk=request.user.id)
		product = Product.objects.filter(is_active=True)
		image = Image.objects.filter(id=product)
		category = Category.objects.all()
		gender = Gender.objects.all()

	return render(request, 'allproducts.html', {'customer': customer, 'product': product, 'image': image, 'c': c,
		'category': category, 'gender': gender})

def productdetails(request, pk):
	if request.user.is_Customer:
		customer = MyUser.object.get(pk=request.user.id)
		product = Product.objects.filter(pk=pk)
		pid = Product.objects.get(pk=pk)
		image = Image.objects.get(pid=product)
		category = Category.objects.all()
		shopowner = MyUser.object.filter(product=product)
		shop = Shop.objects.get(sid=shopowner)

		if request.method == 'POST':
			print "data added to cart"
			customer.cart_set.create(cuid=customer, pid=pid, shop=shop, purdate=timezone.now())
			return redirect('cart')		

	return render(request, 'productdetails.html', {'customer': customer, 'product': product, 'image': image, 'category': category})

def cart(request):
	if request.user.is_Customer:
		customer = MyUser.object.get(pk=request.user.id)
		cart = Cart.objects.filter(cuid=customer).values('shop', 'pid', 'purdate')
		product = Product.objects.filter(is_active=True)
	return render(request, 'cart.html', {'customer': customer, 'cart': cart, 'product': product})

def checkout(request):
	if request.user.is_Customer:
		customer = MyUser.object.get(pk=request.user.id)
	return render(request, 'checkout.html')

##################### FILTER PRODUCTS BY GENDER ############################
##################### FILTER PRODUCTS BY GENDER ############################
##################### FILTER PRODUCTS BY GENDER ############################

def productbygender(request,gid):
	if request.user.is_Customer:
		gender = Gender.objects.filter(pk=gid)
		product = Product.objects.filter(is_active=True, sex=gid)
		c = Product.objects.filter(is_active=True, sex=gid).count()
		
		category = Category.objects.all()
		return render(request, 'productsbygender.html', {'product': product, 'category': category, 'gender': gender, 'c': c})

# def tshirts(request):
# 	return render(request, 'tshirts.html')

##################### FILTER PRODUCTS BY CATEGORY ##########################
##################### FILTER PRODUCTS BY CATEGORY ##########################
##################### FILTER PRODUCTS BY CATEGORY ##########################

def productbycategory(request,cid):
	if request.user.is_Customer:
		product = Product.objects.filter(is_active=True, cid=cid)
		c = Product.objects.filter(is_active=True, cid=cid).count()
		gender = Gender.objects.all()
		category = Category.objects.all()
		cname = Category.objects.filter(pk=cid)
		return render(request, 'productbycategory.html', {'product': product, 'gender': gender, 'category': category, 'cname': cname, 'c': c})

################ FILTER PRODUCTS BY GENDER AND CATEGORY ####################
################ FILTER PRODUCTS BY GENDER AND CATEGORY ####################
################ FILTER PRODUCTS BY GENDER AND CATEGORY ####################

def productbygenderandcategory(request, gid,cid):
	if request.user.is_Customer:
		product = Product.objects.filter(is_active=True, sex=gid, cid=cid)
		category = Category.objects.all()
		gender = Gender.objects.filter(pk=gid)
		return render(request, 'productbygenderandcategory.html', {'product': product, 'category': category, 'gender': gender})

########################## SHOP OF SHOPOWNER ##############################
########################## SHOP OF SHOPOWNER ##############################
########################## SHOP OF SHOPOWNER ##############################

def shops(request):
	if request.user.is_Customer:
		shop = Shop.objects.filter(is_active=True)
		return render(request, 'shop/shopshomepage.html', {'shop': shop})

def productbyshop(request, shid):
	category = Category.objects.all()
	gender = Gender.objects.all()
	product = Product.objects.filter(is_active=True, shop=shid)
	shop = Shop.objects.filter(pk=shid)

	return render(request, 'shop/allproductinshop.html', {'product': product, 'category': category, 'gender': gender, 'shop': shop})

def productinshopbygender(request,shid, sid):
	product = Product.objects.filter(is_active=True, shop=shid, sex=sid)
	category = Category.objects.all()
	gender = Gender.objects.filter(pk=sid)
	shop = Shop.objects.filter(pk=shid)

	return render(request, 'shop/productinshopbygender.html', {'product': product, 'gender': gender, 'category': category, 'shop': shop})

def productinshopandcategory(request, shid, cid):
	product = Product.objects.filter(is_active=True, shop=shid, cid=cid)
	category = Category.objects.all()
	gender = Gender.objects.all()
	shop = Shop.objects.filter(pk=shid)
	return render(request, 'shop/productinshopbycategory.html', {'product': product, 'gender': gender, 'category': category, 'shop': shop})

def productinshopbygenderandcategory(request, shid, sid, cid):
	product = Product.objects.filter(is_active=True, shop=shid, sex=sid, cid=cid )
	gender = Gender.objects.filter(pk=sid)
	category = Category.objects.all()
	shop = Shop.objects.filter(pk=shid)
	return render(request, 'shop/productinshopbygenderandcategory.html', {'shop': shop, 'product': product, 'gender': gender, 'category': category})