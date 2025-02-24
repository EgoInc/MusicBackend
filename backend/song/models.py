from django.db import models

class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)
    year = models.IntegerField()
    yandex_music_link = models.CharField(max_length=255)

    def __str__(self):
        return f"Песня {self.title} (ID: {self.id}) выпущена в {self.date_of_birth} году. Cлушать на ЯндексМузыке - {self.yandex_music_link}"
