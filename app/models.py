import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class Profile(models.Model):

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    user = models.OneToOneField(User, related_name='Profile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def email(self):
        return self.user.email

    @receiver(post_save, sender=User)
    def update_perfil(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(usuario=instance)
            # Carteira.objects.create(perfil=Perfil.objects.latest('id'), saldo=10)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.perfil.save()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Musician(models.Model):

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    birthday = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Artist(models.Model):

    name = models.CharField(max_length=255, null=False)
    since = models.DateTimeField(auto_now=False)
    musicians = models.ManyToManyField('Musician', through='GroupMember', related_name='people')

    def __str__(self):
        return self.name


class GroupMember(models.Model):

    artist = models.ForeignKey(Artist, related_name='artist_musicians', on_delete=models.CASCADE)
    musician = models.ForeignKey(Musician, related_name='musician_artists', on_delete=models.CASCADE)


class Label(models.Model):
    name = models.CharField(max_length=255, null=False)


class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)


class Album(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist_albums')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='label_albums')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre_albums')
    title = models.CharField(max_length=255, null=False)
    year = models.DateTimeField(auto_now=False)


class Track(models.Model):

    number = models.IntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_tracks')
    length = models.CharField(max_length=5, null=False)


class AlbumReview(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_reviews')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_reviews')
    review = models.CharField(max_length=255, null=False)
    rank = models.IntegerField(default=0)


class TrackReview(models.Model):

    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name='album_review_tracks')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='track_reviews')
    review = models.CharField(max_length=255, null=False)
