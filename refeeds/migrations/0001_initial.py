# Generated by Django 4.0.2 on 2022-02-28 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('url', models.URLField()),
                ('last_scrape', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('hash', models.CharField(default=None, max_length=64, unique=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refeeds.feed')),
            ],
        ),
    ]