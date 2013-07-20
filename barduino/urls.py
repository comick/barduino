from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login$', 'barduino.views.login', 'login'),
    url(r'^parties$', 'barduino.views.parties', 'parties'),
    url(r'^tubi$', 'barduino.views.tubi')
    # Examples:
    # url(r'^$', 'barduino.views.home', name='home'),
    # url(r'^barduino/', include('barduino.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
