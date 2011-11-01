from musicplaylistapp.music.models import Musician, Band_Artists, Album, Song

def homepage(request):
    song = Song.objects.order_by('title')
    band_artists = Band_Artists.objects.order_by('name')
    album = Album.objects.order_by('title')
    return render_to_response(homepage.html', {
        'song': song,
        'band_artist': band_artists
        'album': album
    })


