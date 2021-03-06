from django.conf.urls import patterns, url
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings

############################################################################
############################################################################
########################     ADMIN          ################################
urlpatterns = patterns('',
	url(r'^admin/dashboard/$', 'app.views.admin_dashboard', name='admin_dashboard'),
	url(r'^admin/user/add/$', 'app.views.add_user', name='add_user'),
	url(r'^admin/category/$', 'app.views.add_category', name='add_category'),
	url(r'^admin/product/add/$', 'app.views.add_product', name='add_product')





)

############################################################################
############################################################################
########################     REGISTRATION   ################################
urlpatterns += patterns('',
    url(r'^register/$', 'app.views.register_user', name='register_user'),
    url(r'^register_done/$', 'app.views.register_done', name='register_done'),
    url(r'^login/$', 'app.views.login_user', name='login_user'),
    url(r'^logout/$', 'app.views.logout_user', name='logout_user'),
    url(r'^shopowner/dashboard/$', 'app.views.shopowner_dashboard', name='shopowner_dashboard'),
    url(r'^shop/$', 'app.views.shop', name='shop'),
    url(r'^home/$', 'app.views.home', name='home'),
    url(r'^login_error/$', 'app.views.login_error', name='login_error'),


    





)

############################################################################
############################################################################
########################     Customer       ################################
urlpatterns += patterns('',
	url(r'^shop/clothing/$', 'app.views.allproducts', name='allproducts'),
	url(r'^shop/clothing/details/(?P<pk>\d+)/$', 'app.views.productdetails', name='productdetails'),
	url(r'^cart/$', 'app.views.cart', name='cart'),
	url(r'^shop/clothing/gender/(?P<gid>\d+)/$', 'app.views.productbygender', name='productbygender'),
	url(r'^shop/clothing/category/(?P<cid>\d+)/$', 'app.views.productbycategory', name='productbycategory'),
	url(r'^shop/clothing/gender/category/(?P<gid>\d+)/(?P<cid>\d+)/$', 'app.views.productbygenderandcategory', name='productbygenderandcategory'),
	url(r'^shop/clothing/(?P<shid>\d+)/$', 'app.views.productbyshop', name='productbyshop'),
	url(r'^shops/$', 'app.views.shops', name='shops'),
	url(r'^shop/clothing/shop/gender/(?P<shid>\d+)/(?P<sid>\d+)/$', 'app.views.productinshopbygender', name='productinshopbygender'),
	url(r'^shop/clothing/shop/category/(?P<shid>\d+)/(?P<cid>\d+)/$', 'app.views.productinshopandcategory', name='productbyshopandcategory'),
	url(r'^shop/clothing/shop/gender/category/(?P<shid>\d+)/(?P<sid>\d+)/(?P<cid>\d+)/$', 'app.views.productinshopbygenderandcategory', name='productinshopbygenderandcategory'),


)

############################################################################
############################################################################
########################     SHOPOWNER      ################################
urlpatterns += patterns('',
	url(r'^shopowner/dashboard/$', 'app.views.shopowner_dashboard', name='shopowner_dashboard'),
	url(r'^shopowner/product/add/$', 'app.views.sadd_product', name='sadd_product'),
	url(r'^shopowner/product/view/$', 'app.views.sview_product', name='sview_product'),
	url(r'^shopowner/product/view/(?P<pk>\d+)/$', 'app.views.sview_productdetails', name='sview_productdetails' ),
	url(r'^shopowner/category/$', 'app.views.sview_category', name='sview_category'),
	url(r'^shopowner/category/(?P<category_id>\d+)/$', 'app.views.sview_productbycategory', name='sview_productbycategory'),
	url(r'^shopowner/product/update/(?P<pk>\d+)/$', 'app.views.supdate_product', name='supdate_product'),
	url(r'^shopowner/product/delete/(?P<pk>\d+)/$', 'app.views.sdelete_product', name='sdelete_product'),
	url(r'^shopowner/settings/$', 'app.views.ssettings', name='ssettings'),
	url(r'^shopowner/settings/update/profile/$', 'app.views.ssupdate_profile', name='ssupdate_profile'),
	url(r'^shopowner/settings/update/billingaddress/$', 'app.views.ssupdate_billingaddress', name='ssupdate_billingaddress'),
	url(r'^shopowner/settings/update/permanentaddress/$', 'app.views.ssupdate_permanentaddress', name='ssupdate_permanentaddress'),
	url(r'^shopowner/settings/update/shopname/$', 'app.views.shopname', name='shopname'),
	url(r'^sorder/$', 'app.views.sorder', name='sorder'),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#for photo upload

urlpatterns += [
    url(r'^password_change/$', views.password_change, name='password_change_form'),
    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'), 
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset_done/$', views.password_reset_done, name='password_reset_done' ),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset_complete/$', views.password_reset_complete, name='password_reset_complete'),    
] 