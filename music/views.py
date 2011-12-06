from musicplaylistapp.music.models import Musician, Band_Artists, Album, Song, NowPlaying
from django.shortcuts import render_to_response

def homepage(request):
    song = NowPlaying.objects.order_by('-playtime')[:1]
    band_artists = Band_Artists.objects.order_by('name')
    album = Album.objects.order_by('title')
    return render_to_response('homepage.html', {
        'song': song,
        'band_artist': band_artists,
        'album': album,
    })

def band_artist(request):
    album = Album.objects.order_by('title')
    songs = Song.objects.order_by('track_number')
    return render_to_response('album.html',{
        'album': album,
        'song': song,
    })

def songlist2(request):
    songs = Song.objects.order_by('title')
    return render_to_response('songlist2.html', {
        'songs' : songs,
    })


def songdetail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render_to_response('song_detail.html', {
        'song' : song,
    })

def songlist(request):
    song = NowPlaying.objects.order_by('-playtime')[:25]
    return render_to_response('songlist.html', {
        'song' : song,
    })

def band_artistsdetail(request, band_artists_id):
    band_artists = Band_Artists.objects.get(id=band_artists_id)
    albums = Album.objects.filter(band_artist=band_artists)
    return render_to_response('band_artists_detail.html', {
        'band_artists' : band_artists,
        'albums' : albums,
    })

def band_artistlist(request):
    band_artists = Band_Artists.objects.order_by('name')
    return render_to_response('band-artistlist.html', {
        'band_artists' : band_artists,
    })

def albumdetail(request, album_id):
    album = Album.objects.get(id=album_id)
    songs = Song.objects.filter(album=album).order_by('track_number')
    return render_to_response('album_detail.html', {
        'album' : album,
        'songs' : songs,
    })

def albumlist(request):
    album = Album.objects.order_by('title')
    return render_to_response('albumlist.html', {
        'album' : album,
    })
