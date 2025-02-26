from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from .models import Clip
from .serializers import ClipSerializer

class ClipListView(APIView):
    @extend_schema(
        summary="Получить список клипов",
        description="Возвращает список всех клипов из базы данных.",
        responses={200: ClipSerializer(many=True)}
    )
    def get(self, request):
        clips = Clip.objects.all()
        serializer = ClipSerializer(clips, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    permission_classes = [permissions.IsAdminUser]
    @extend_schema(
        summary="Добавить новый клип",
        description="Создает новый клип в базе данных.",
        request=ClipSerializer,
        responses={201: ClipSerializer}
    )
    def post(self, request):
        serializer = ClipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClipDetailView(APIView):
    @extend_schema(
        summary="Получить один клип",
        description="Возвращает клип по ID из базы данных.",
        responses={200: ClipSerializer}
    )
    def get(self, request, clip_id):
        try:
            clip = Clip.objects.get(id=clip_id)
            serializer = ClipSerializer(clip)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Clip.DoesNotExist:
            return Response({"error": "Клип не найден"}, status=status.HTTP_404_NOT_FOUND)

    permission_classes = [permissions.IsAdminUser]
    @extend_schema(
        summary="Обновить клип",
        description="Изменяет данные клипа по ID в базе данных.",
        request=ClipSerializer,
        responses={200: ClipSerializer}
    )
    def put(self, request, clip_id):
        try:
            clip = Clip.objects.get(id=clip_id)
            serializer = ClipSerializer(clip, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Clip.DoesNotExist:
            return Response({"error": "Клип не найден"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Удалить клип",
        description="Удаляет клип по ID из базы данных.",
        responses={204: "Клип удален"}
    )
    def delete(self, request, clip_id):
        try:
            clip = Clip.objects.get(id=clip_id)
            clip.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Clip.DoesNotExist:
            return Response({"error": "Клип не найден"}, status=status.HTTP_404_NOT_FOUND)
