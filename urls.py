from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$', 'musicplaylistapp.music.views.homepage'),
    (r'song/$', 'musicplaylistapp.music.views.song_list'),
    #(r'song/$', 'musicplaylistapp.music.views.song_detail'),
    # url(r'^musicplaylistapp/', include('musicplaylistapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
