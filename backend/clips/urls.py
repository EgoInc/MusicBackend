from django.urls import path
from .views import ClipListView, ClipDetailView

urlpatterns = [
    path('clips/', ClipListView.as_view(), name='clip-list'),
    path('clips/<int:clip_id>/', ClipDetailView.as_view(), name='clip-detail'),
]
