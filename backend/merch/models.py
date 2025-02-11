from django.db import models

class Merch(models.Model):
    CATEGORY_CHOICES = [
        ('футболка', 'Футболка'),
        ('кепка', 'Кепка'),
        ('толстовка', 'Толстовка'),
        ('кружка', 'Кружка'),
        ('аксессуар', 'Аксессуар'),
        # тут можно другие категории добавить при необходимости
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    purchase_link = models.URLField(blank=True, null=True, verbose_name="Ссылка для покупки")
    size = models.CharField(max_length=50, blank=True, null=True, verbose_name="Размер")

    def __str__(self):
        return self.name


class MerchImage(models.Model):
    merch = models.ForeignKey(Merch, related_name='images', on_delete=models.CASCADE, verbose_name="Товар")
    image = models.ImageField(upload_to='merch_images/', verbose_name="Изображение")

    def __str__(self):
        return f"Изображение для {self.merch.name}"