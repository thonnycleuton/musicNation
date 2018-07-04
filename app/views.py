import django_filters
from rest_framework import permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from app.models import *
from app.permissions import IsOwnerOrReadOnly
from app.serializers import *


class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('album__artist', )
    search_fields = ('name', 'album__artist', )
    ordering_fields = ('name', 'number', )


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAdminUser,)


class MusicianViewSet(ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter, )
    ordering_fields = ('name', )


class GroupMemberViewSet(ModelViewSet):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = (permissions.IsAdminUser,)


class LabelViewSet(ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('artist', )
    search_fields = ('title', 'artist', )
    ordering_fields = ('title', )


class AlbumReviewViewSet(ModelViewSet):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)


class APIRoot(APIView):

    def get(self, request):
        data = {
            "profiles": "http://localhost:8000/profiles/",
            "tracks": "http://localhost:8000/tracks/",
            "musicians": "http://localhost:8000/musicians/",
            "artists": "http://localhost:8000/artists/",
            "groupmembers": "http://localhost:8000/groupmembers/",
            "labels": "http://localhost:8000/labels/",
            "genres": "http://localhost:8000/genres/",
            "albums": "http://localhost:8000/albums/",
            "albumreviews": "http://localhost:8000/albumreviews/",
        }
        return Response(data)
