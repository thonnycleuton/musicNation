from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

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
    path('cliente/', TemplateView.as_view(template_name='index.html')),
    # JWT auth
    url(r'^auth/obtain_token/', obtain_jwt_token),
    url(r'^auth/refresh_token/', refresh_jwt_token),
]

urlpatterns += router.urls
