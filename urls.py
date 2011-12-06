from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$', 'musicplaylistapp.music.views.homepage'),
    (r'^band-artist/$', 'musicplaylistapp.music.views.band_artistlist'),
    (r'^band-artist/(?P<band_artists_id>\d+)/$', 'musicplaylistapp.music.views.band_artistsdetail'),
    (r'^album/$', 'musicplaylistapp.music.views.albumlist'),
    (r'^album/(?P<album_id>\d+)/$', 'musicplaylistapp.music.views.albumdetail'),
    (r'^song/$', 'musicplaylistapp.music.views.songlist'),
    (r'^song/(?P<song_id>\d+)/$', 'musicplaylistapp.music.views.songdetail'),
    (r'song_list/$', 'musicplaylistapp.music.views.songlist2'),
    # url(r'^musicplaylistapp/', include('musicplaylistapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
