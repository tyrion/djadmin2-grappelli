from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import djadmin2
djadmin2.default.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin2/', include(djadmin2.default.urls)),
)
