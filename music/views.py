from musicplaylistapp.music.models import Musician, Band_Artists, Album, Song
from django.shortcuts import render_to_response

def homepage(request):
    song = Song.objects.order_by('title')
    band_artists = Band_Artists.objects.order_by('name')
    album = Album.objects.order_by('title')
    return render_to_response('homepage.html', {
        'song': song,
        'band_artist': band_artists,
        'album': album,
    })

def song_list(request):
    album = Album.objects.order_by('title')
    band_artists = Band_Artists.objects.order_by('name')
    songs = Song.objects.order_by('title')
    return render_to_response('song_list.html', {
        'album' : album,
        'band_artists' : band_artists,
        'song' : song,
    })

