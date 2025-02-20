# Generated by Django 5.1.6 on 2025-02-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('yandex_music_link', models.CharField(max_length=255)),
            ],
        ),
    ]
