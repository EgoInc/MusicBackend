from django.db import models

class Clip(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название клипа")
    url = models.URLField(verbose_name="Ссылка на видео")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
