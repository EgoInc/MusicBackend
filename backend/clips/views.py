from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .models import Clip
from .serializers import ClipSerializer

# Заглушечные данные
CLIPS = [
    {"id": 1, "title": "Клип 1", "url": "https://example.com/video1"},
    {"id": 2, "title": "Клип 2", "url": "https://example.com/video2"},
]

class ClipListView(APIView):
    @extend_schema(
        summary="Получить список клипов",
        description="Возвращает список всех клипов.",
        responses={200: ClipSerializer(many=True)}
    )
    def get(self, request):
        return Response(DUMMY_CLIPS, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Добавить новый клип",
        description="Создает новый клип.",
        request=ClipSerializer,
        responses={201: ClipSerializer}
    )
    def post(self, request):
        new_clip = request.data
        new_clip["id"] = len(CLIPS) + 1
        CLIPS.append(new_clip)
        return Response(new_clip, status=status.HTTP_201_CREATED)

class ClipDetailView(APIView):
    @extend_schema(
        summary="Получить один клип",
        description="Возвращает клип по ID.",
        responses={200: ClipSerializer}
    )
    def get(self, request, clip_id):
        clip = next((c for c in CLIPS if c["id"] == clip_id), None)
        if clip:
            return Response(clip, status=status.HTTP_200_OK)
        return Response({"error": "Клип не найден"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Обновить клип",
        description="Изменяет данные клипа по ID.",
        request=ClipSerializer,
        responses={200: ClipSerializer}
    )
    def put(self, request, clip_id):
        for clip in CLIPS:
            if clip["id"] == clip_id:
                clip.update(request.data)
                return Response(clip, status=status.HTTP_200_OK)
        return Response({"error": "Клип не найден"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Удалить клип",
        description="Удаляет клип по ID.",
        responses={204: "Клип удален"}
    )
    def delete(self, request, clip_id):
        global CLIPS
        CLIPS = [clip for clip in CLIPS if clip["id"] != clip_id]
        return Response(status=status.HTTP_204_NO_CONTENT)
