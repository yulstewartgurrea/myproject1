from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^register/$', 'app.views.register_user', name='register_user'),
    url(r'^register/$', 'app.views.register_done', name='register_done'),
    url(r'^login/$', 'app.views.login_user', name='login_user'),
    url(r'^logout/$', 'app.views.logout_user', name='logout_user'),
    url(r'^admin/dashboard/$', 'app.views.admin_dashboard', name='admin_dashboard'),
    url(r'^shopowner/dashboard/$', 'app.views.shopowner', name='shopowner'),
    url(r'^customer/$', 'app.views.customer', name='customer'),
    url(r'^home/$', 'app.views.home', name='home'),

############################################################################
############################################################################
########################     ADMIN       ###################################
    
############################################################################
############################################################################
########################     SHOPOWNER      ################################

############################################################################
############################################################################
########################     CUSTOMER       ################################
)