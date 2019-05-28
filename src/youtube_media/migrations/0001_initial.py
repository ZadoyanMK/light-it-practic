# Generated by Django 2.0 on 2019-05-28 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_count', models.IntegerField(db_index=True, default=0)),
                ('url', models.CharField(max_length=512)),
                ('hash_url', models.CharField(db_index=True, max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='RequestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_count', models.IntegerField(db_index=True, default=0)),
                ('data', models.CharField(max_length=512)),
                ('hash_data', models.CharField(db_index=True, max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='RequestLinkConn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_media.Links')),
                ('request_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_media.RequestData')),
            ],
        ),
        migrations.AddField(
            model_name='featured',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_media.Links'),
        ),
        migrations.AddField(
            model_name='featured',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]