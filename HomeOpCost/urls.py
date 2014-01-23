from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HomeOpCost.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', 'app.views.index'),
    url(r'^create', 'app.views.createUser'),
    url(r'^changePassword', 'app.views.changePassword'),
    url(r'^login', 'app.views.login'),
    url(r'^logout', 'app.views.logout'),
)
