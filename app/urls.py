from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'tracks', TrackViewSet, base_name='track')
router.register(r'profiles', ProfileViewSet, base_name='profile')
router.register(r'musicians', MusicianViewSet, base_name='musician')
router.register(r'artists', ArtistViewSet, base_name='artist')
router.register(r'groupmembers', GroupMemberViewSet, base_name='groupmember')
router.register(r'labels', LabelViewSet, base_name='label')
router.register(r'genres', GenreViewSet, base_name='genre')
router.register(r'albums', AlbumViewSet, base_name='album')
router.register(r'albumreviews', AlbumReviewViewSet, base_name='albumreview')

urlpatterns = [
    url(r'^$', APIRoot.as_view(), name='root'),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls
