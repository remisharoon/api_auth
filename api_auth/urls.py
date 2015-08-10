from django.conf.urls import patterns, include, url
from django.contrib import admin
from api_auth.api_rest import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api_auth.views.home', name='home'),
    # url(r'^api_auth/', include('api_auth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/?$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/?$', views.UserDetail.as_view()),    
)
