# Generated by Django 2.2 on 2019-06-02 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='etag',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='requestdata',
            name='etag',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
