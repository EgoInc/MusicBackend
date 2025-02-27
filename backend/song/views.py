from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Song
from .serializers import SongSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes 


class SongListView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        summary="Получить все песни",
        description="Возвращает список всех песен из БД.",
        responses={200: SongSerializer(many=True)}
    )
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Добавить новую песню",
        description="Добавляет информацию о новой песне в БД.",
        request=SongSerializer,
        responses={201: SongSerializer}
    )
    def post(self, request):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetailView(APIView):
    @extend_schema(
        summary="Получить песню",
        description="Возвращает песню из БД по ID.",
        responses={200: SongSerializer}
    )
    def get(self, request, song_id):
        try:
            song = Song.objects.get(id=song_id)
            serializer = SongSerializer(song)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except song.DoesNotExist:
            return Response({"response": "Песня не найдена"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Обновить информауию о песне",
        description="Изменяет данные песни в БД по ее ID.",
        request=SongSerializer,
        responses={200: SongSerializer}
    )
    def put(self, request, song_id):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            song = Song.objects.get(id=song_id)
            serializer = SongSerializer(song, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except song.DoesNotExist:
            return Response({"response": "Пеня не найдена"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Удалить песню",
        description="Удаляет песню из БД по ее ID.",
        responses={204: "Пеня удалена"}
    )
    def delete(self, request, song_id):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            song = Song.objects.get(id=song_id)
            song.delete()
            return Response({"response": "Песня удалена"}, status=status.HTTP_204_NO_CONTENT)
        except song.DoesNotExist:
            return Response({"response": "Пеня не найдена"}, status=status.HTTP_404_NOT_FOUND)