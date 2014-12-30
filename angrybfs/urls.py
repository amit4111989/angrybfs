from django.conf.urls import patterns, include, url
from django.contrib import admin
from signup import views
from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'angrybfs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', include(main.site.urls)),
    url(r'^signup/', include(main.site.urls)),
)
