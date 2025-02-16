from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import SongListView, SongDetailView


urlpatterns = [
    path('songs/', SongListView.as_view(), name='song-list'),
    path('songs/<int:song_id>/', SongDetailView.as_view(), name='song-detail'),
]

