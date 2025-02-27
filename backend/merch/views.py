from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from .serializers import MerchSerializer
from .models import Merch
from django.shortcuts import get_object_or_404

class MerchListView(APIView):
    @extend_schema(
        summary="Получить список товаров",
        description="Возвращает список всех товаров с возможностью фильтрации по категории, размеру и сортировки по цене.",
        parameters=[
            OpenApiParameter(name='category', type=OpenApiTypes.STR, description='Фильтр по категории'),
            OpenApiParameter(name='size', type=OpenApiTypes.STR, description='Фильтр по размеру'),
            OpenApiParameter(name='ordering', type=OpenApiTypes.STR, description='Сортировка по полю'),
        ],
        responses={status.HTTP_200_OK: MerchSerializer(many=True)},
    )
    def get(self, request):
        queryset = Merch.objects.all()

        # Фильтрация
        category = request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        size = request.query_params.get('size')
        if size:
            queryset = queryset.filter(size=size)

        # Сортировка
        ordering = request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)

        serializer = MerchSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    permission_classes = [permissions.IsAdminUser]
    @extend_schema(
        summary="Добавить новый товар",
        description="Создает новый товар с указанными параметрами.",
        request=MerchSerializer,
        responses={status.HTTP_201_CREATED: MerchSerializer},
    )
    def post(self, request):
        serializer = MerchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MerchDetailView(APIView):
    @extend_schema(
        summary="Получить информацию о товаре",
        description="Возвращает полную информацию о товаре по его ID.",
        responses={status.HTTP_200_OK: MerchSerializer, status.HTTP_404_NOT_FOUND: "Товар не найден"},
    )
    def get(self, request, merch_id):
        merch = get_object_or_404(Merch, pk=merch_id)
        serializer = MerchSerializer(merch)
        return Response(serializer.data, status=status.HTTP_200_OK)

    permission_classes = [permissions.IsAdminUser]
    @extend_schema(
        summary="Обновить товар",
        description="Заменяет все данные товара новыми значениями.",
        request=MerchSerializer,
        responses={status.HTTP_200_OK: MerchSerializer, status.HTTP_404_NOT_FOUND: "Товар не найден"},
    )
    def put(self, request, merch_id):
        merch = get_object_or_404(Merch, pk=merch_id)
        serializer = MerchSerializer(merch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Частично обновить товар",
        description="Изменяет только указанные поля товара.",
        request=MerchSerializer,
        responses={status.HTTP_200_OK: MerchSerializer, status.HTTP_404_NOT_FOUND: "Товар не найден"},
    )
    def patch(self, request, merch_id):
        merch = get_object_or_404(Merch, pk=merch_id)
        serializer = MerchSerializer(merch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Удалить товар",
        description="Удаляет товар по указанному ID.",
        responses={status.HTTP_204_NO_CONTENT: "Товар успешно удален", status.HTTP_404_NOT_FOUND: "Товар не найден"},
    )
    def delete(self, request, merch_id):
        merch = get_object_or_404(Merch, pk=merch_id)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
