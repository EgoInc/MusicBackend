from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SongSerializer


class SongListView(APIView):
    @extend_schema(
        summary="Получить список всех песен",
        description="Возвращает список всех песен в базе данных.",
        responses={status.HTTP_200_OK: SongSerializer(many=True)},
    )
    def get(self, request):
        # Заглушка данных TODO: сделать обращение к базе
        songs = [
            {
                "song_id": 1,
                "title": "Love Sosa",
                "cover": "http://example/new_cover.jpg",
                "year": 2018,
                "yandex_music_link": "https//yandex..." 
            },
            {
                "song_id": 2,
                "title": "Type Shit",
                "cover": "http://example/new_cover.jpg",
                "year": 2023,
                "yandex_music_link": "https//yandex..." 
            }
        ]
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    @extend_schema(
        summary="Добавить песню",
        description="Позволяет добавить новую песню в базу данных.",
        request=SongSerializer,
        responses={status.HTTP_201_CREATED: SongSerializer},
    )
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Заглушка данных TODO: сделать обработку запроса        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SongDetailView(APIView):
    @extend_schema(
        summary="Изменить песню",
        description="Позволяет изменить данные существующей песни по её ID.",
        request=SongSerializer,
        responses={status.HTTP_200_OK: SongSerializer},
    )
    def put(self, request, song_id):
        song = {
            "song_id": song_id,
            "title": "Just Wanna Rock",
            "cover": "http://example/new_cover.jpg",
            "year": 2021,
            "yandex_music_link": "https://music.yandex.ru..."
        }
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Заглушка данных TODO: сделать обработку запроса        
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Удалить песню",
        description="Удаляет песню по её ID.",
        responses={status.HTTP_204_NO_CONTENT: None},
    )
    def delete(self, request, song_id):
        return Response(status=status.HTTP_204_NO_CONTENT)
