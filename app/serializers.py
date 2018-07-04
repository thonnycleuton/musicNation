from rest_framework import serializers
from app.models import *


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'first_name', 'last_name',)


class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class GroupMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupMember
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AlbumReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlbumReview
        fields = '__all__'


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    album_tracks = TrackSerializer(many=True, read_only=True)
    album_reviews = AlbumReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = '__all__'
