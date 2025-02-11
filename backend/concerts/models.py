from django.db import models

# Create your models here.
class Concert(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Ожидается'),
        ('past', 'Прошел')
    ]

    date = models.DateField(verbose_name="Дата концерта")
    city = models.CharField(max_length=100, verbose_name="Город")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Статус')
    ticket_link = models.URLField(verbose_name="Ссылка на билеты", blank=True, null=True)

    def __str__(self):
        return f"{self.date} {self.city} {self.status}"