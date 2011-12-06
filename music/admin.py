from music.models import Musician, Album, Band_Artists, Song, NowPlaying
from django.contrib import admin

class MusicianAdmin(admin.ModelAdmin):
    fields = ['last_name', 'first_name', 'gender', 'country']


admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album)
admin.site.register(Band_Artists)
admin.site.register(Song)
admin.site.register(NowPlaying)
