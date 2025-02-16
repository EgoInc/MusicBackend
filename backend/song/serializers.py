from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['song_id', 'title', 'cover', 'year', 'yandex_music_link']


