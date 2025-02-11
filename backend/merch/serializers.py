from rest_framework import serializers
from .models import Merch, MerchImage

class MerchImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchImage
        fields = ['id', 'image']

class MerchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    purchase_link = serializers.URLField(required=False, allow_blank=True)
    size = serializers.CharField(required=False, allow_blank=True)
    # предполагается, что картинки может не быть при создании
    images = MerchImageSerializer(many=True, read_only=True, required=False)


    def create(self, validated_data):
         return Merch.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.purchase_link = validated_data.get('purchase_link', instance.purchase_link)
        instance.size = validated_data.get('size', instance.size)
        instance.save()
        return instance