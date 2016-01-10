from django.conf.urls import patterns, url

############################################################################
############################################################################
########################     ADMIN          ################################
urlpatterns = patterns('',
	url(r'^admin/dashboard/$', 'app.views.admin_dashboard', name='admin_dashboard'),
	url(r'^admin/user/add/$', 'app.views.add_user', name='add_user'),
	url(r'^admin/category/$', 'app.views.add_category', name='add_category')





)


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
########################     SHOPOWNER      ################################

############################################################################
############################################################################
########################     SHOP           ################################

############################################################################
############################################################################
########################     REGISTRATION   ################################
)


