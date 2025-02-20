from django.db import models

class Song(models.Model):
    song_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    cover = models.URLField()
    year = models.IntegerField()
    yandex_music_link = models.URLField()

    def __str__(self):
        return f"Песня {self.title} (ID: {self.id}) выпущена в {self.date_of_birth} году. Cлушать на ЯндексМузыке - {self.yandex_music_link}"

    class Meta:
        app_label = 'song'
