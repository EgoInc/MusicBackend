# Generated by Django 4.2.10 on 2025-02-27 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Merch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("футболка", "Футболка"),
                            ("кепка", "Кепка"),
                            ("толстовка", "Толстовка"),
                            ("кружка", "Кружка"),
                            ("аксессуар", "Аксессуар"),
                        ],
                        max_length=50,
                        verbose_name="Категория",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Название")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена"
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                (
                    "purchase_link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Ссылка для покупки"
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Размер"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MerchImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="merch_images/", verbose_name="Изображение"
                    ),
                ),
                (
                    "merch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="merch.merch",
                        verbose_name="Товар",
                    ),
                ),
            ],
        ),
    ]
