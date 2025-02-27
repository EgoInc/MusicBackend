from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Song(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=255, verbose_name="Название")
    cover = models.URLField(verbose_name="Обложка")
    year = models.IntegerField(
        verbose_name="Год выпуска",
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year)
        ]
    )
    yandex_music_link = models.URLField(verbose_name="Ссылка на трек в Яндекс Музыке")

    class Meta:
        app_label = 'song'

    def __str__(self):
        return self.title
