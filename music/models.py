from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(max_length=200)
    position = models.CharField(max_length=200)


class Band_Artists(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Musician)
    country = models.CharField(max_length=200)
    
    def get_absolute_url(self):
        return "/band-artist/%i/" % self.id

    def __unicode__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    year_released = models.DateField()
    num_stars = models.IntegerField()
    band_artist = models.ManyToManyField(Band_Artists)
    genre = models.CharField(max_length=100)
    length = models.TimeField()

    def get_absolute_url(self):
        return "/album/%i/" % self.id

    def __unicode__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=200)
    track_number = models.IntegerField()
    length = models.TimeField()
    album = models.ManyToManyField(Album)

    def get_absolute_url(self):
        return "/music/%i/" % self.id

    def __unicode__(self):
        return self.title
