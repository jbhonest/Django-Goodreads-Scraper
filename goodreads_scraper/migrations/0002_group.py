# Generated by Django 4.2 on 2024-02-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodreads_scraper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('members', models.IntegerField()),
                ('cover_image_url', models.URLField()),
            ],
        ),
    ]