from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from .serializers import ConcertSerializer


class ConcertListView(APIView):
    @extend_schema(
        summary="Получить список концертов",
        description="Возвращает список всех концертов с датой, городом, статусом и ссылкой на билеты.",
        responses={status.HTTP_200_OK: ConcertSerializer(many=True)},
    )
    def get(self, request):
        # Заглушка данных TODO: сделать обращение к базе
        concerts = [
            {"id": 1, "city": "Москва", "date": "2024-05-10", "status": "Запланирован", "ticket_link": "https://example.com/tickets/1"},
            {"id": 2, "city": "Санкт-Петербург", "date": "2024-06-15", "status": "Продан", "ticket_link": "https://example.com/tickets/2"},
        ]
        serializer = ConcertSerializer(concerts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Добавить новый концерт",
        description="Создает новый концерт с параметрами (дата, город, статус, ссылка на билеты).",
        request=ConcertSerializer,
        responses={status.HTTP_201_CREATED: ConcertSerializer},
    )
    def post(self, request):
        # Заглушка данных TODO: сделать сохранение в базу
        new_concert = request.data
        new_concert["id"] = 3
        serializer = ConcertSerializer(new_concert)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ConcertDetailView(APIView):
    @extend_schema(
        summary="Получить информацию о концерте",
        description="Возвращает данные концерта по его ID.",
        responses={status.HTTP_200_OK: ConcertSerializer, status.HTTP_404_NOT_FOUND: "Концерт не найден"},
    )
    def get(self, request, concert_id):
        # Заглушка данных TODO: сделать обращение к базе
        concert = {"id": concert_id, "city": "Москва", "date": "2024-05-10", "status": "Запланирован", "ticket_link": "https://example.com/tickets/1"}
        serializer = ConcertSerializer(concert)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Обновить концерт (PUT)",
        description="Заменяет данные концерта новыми значениями.",
        request=ConcertSerializer,
        responses={status.HTTP_200_OK: ConcertSerializer, status.HTTP_404_NOT_FOUND: "Концерт не найден"},
    )
    def put(self, request, concert_id):
        # Заглушка данных TODO: сделать обновление в базе
        updated_concert = request.data
        updated_concert["id"] = concert_id
        serializer = ConcertSerializer(updated_concert)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Частично обновить концерт (PATCH)",
        description="Изменяет только указанные поля концерта.",
        request=ConcertSerializer,
        responses={status.HTTP_200_OK: ConcertSerializer, status.HTTP_404_NOT_FOUND: "Концерт не найден"},
    )
    def patch(self, request, concert_id):
        # Заглушка данных TODO: сделать частичное обновление в базе
        updated_fields = request.data
        updated_fields["id"] = concert_id
        serializer = ConcertSerializer(updated_fields, partial=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Удалить концерт",
        description="Удаляет концерт по указанному ID.",
        responses={status.HTTP_204_NO_CONTENT: "Концерт успешно удален", status.HTTP_404_NOT_FOUND: "Концерт не найден"},
    )
    def delete(self, request, concert_id):
        # Заглушка данных TODO: сделать удаление из базы
        return Response({"message": f"Концерт с ID {concert_id} удален"}, status=status.HTTP_204_NO_CONTENT)
