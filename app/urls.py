from django.conf.urls import patterns, url

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


    


############################################################################
############################################################################
########################     SHOP           ################################


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
	# url(r'^shopowner/product/delete/$', 'app.views.shopowner_dashboard', name='sadd_delete'),

)


