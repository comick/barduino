from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login$', 'barduino.views.login', name='login'),
    url(r'^parties$', 'barduino.views.parties', name='parties'),
    url(r'^tubi$', 'barduino.views.tubi', name='tubi'),
    url(r'^birini$', 'barduino.views.birini', name='birini'),
    url(r'^start$', 'barduino.views.start', name='start'),
    url(r'^q$', 'barduino.views.q', name='q'),
    url(r'^(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', name='static')
    # Examples:
    # url(r'^$', 'barduino.views.home', name='home'),
    # url(r'^barduino/', include('barduino.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
