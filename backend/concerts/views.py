from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from .serializers import ConcertSerializer
from .models import Concert


class ConcertListView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Получить список концертов",
        description="Возвращает список всех концертов с датой, городом, статусом и ссылкой на билеты.",
        responses={status.HTTP_200_OK: ConcertSerializer(many=True)},
    )
    def get(self, request):
        concerts = Concert.objects.all()
        serializer = ConcertSerializer(concerts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Добавить новый концерт",
        description="Создает новый концерт с параметрами (дата, город, статус, ссылка на билеты).",
        request=ConcertSerializer,
        responses={status.HTTP_201_CREATED: ConcertSerializer},
    )
    def post(self, request):
        if not request.user.is_staff:  # Проверяем, является ли пользователь админом
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ConcertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConcertDetailView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Получить информацию о концерте",
        description="Возвращает данные концерта по его ID.",
        responses={status.HTTP_200_OK: ConcertSerializer, status.HTTP_404_NOT_FOUND: "Концерт не найден"},
    )
    def get(self, request, concert_id):
        concert = get_object_or_404(Concert, pk=concert_id)
        serializer = ConcertSerializer(concert)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Обновить концерт (PUT)",
        description="Заменяет данные концерта новыми значениями.",
        request=ConcertSerializer,
        responses={status.HTTP_200_OK: ConcertSerializer, status.HTTP_404_NOT_FOUND: "Концерт не найден"},
    )
    def put(self, request, concert_id):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        concert = get_object_or_404(Concert, pk=concert_id)
        serializer = ConcertSerializer(concert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Частично обновить концерт (PATCH)",
        description="Изменяет только указанные поля концерта.",
        request=ConcertSerializer,
        responses={status.HTTP_200_OK: ConcertSerializer, status.HTTP_404_NOT_FOUND: "Концерт не найден"},
    )
    def patch(self, request, concert_id):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        concert = get_object_or_404(Concert, pk=concert_id)
        serializer = ConcertSerializer(concert, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Удалить концерт",
        description="Удаляет концерт по указанному ID.",
        responses={status.HTTP_204_NO_CONTENT: "Концерт успешно удален", status.HTTP_404_NOT_FOUND: "Концерт не найден"},
    )
    def delete(self, request, concert_id):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        concert = get_object_or_404(Concert, pk=concert_id)
        concert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
