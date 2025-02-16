from django.urls import path
from .views import ConcertListView, ConcertDetailView

urlpatterns = [
    path("concerts/", ConcertListView.as_view(), name="concert-list"),  #Список всех концертов/добавление
    path("concerts/<int:concert_id>/", ConcertDetailView.as_view(), name="concert-detail"),  #Получение/редактирование/удаление
]