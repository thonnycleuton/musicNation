from django.db import models
from django.contrib.auth.models import User


class Profile(User):

    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Musician(models.Model):

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    birthday = models.DateField(auto_now=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Artist(models.Model):

    name = models.CharField(max_length=255, null=False)
    since = models.DateField(auto_now=False)
    musicians = models.ManyToManyField('Musician', through='GroupMember', related_name='people')

    def __str__(self):
        return self.name


class GroupMember(models.Model):

    artist = models.ForeignKey(Artist, related_name='artist_musicians', on_delete=models.CASCADE)
    musician = models.ForeignKey(Musician, related_name='musician_artists', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.artist) + '-' + str(self.musician)


class Label(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Album(models.Model):

    title = models.CharField(max_length=255, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_albums')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='label_albums')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre_albums')
    year = models.DateField(auto_now=False)

    def __str__(self):
        return self.title


class Track(models.Model):

    number = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_tracks')
    length = models.DurationField()

    def __str__(self):
        return self.name


class AlbumReview(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_reviews')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_reviews')
    review = models.CharField(max_length=255, null=False)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.review


class TrackReview(models.Model):

    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name='album_review_tracks')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='track_reviews')
    review = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.review


