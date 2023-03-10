# Generated by Django 4.1.3 on 2022-12-27 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.CharField(default=18, max_length=2)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('duration', models.CharField(max_length=8)),
                ('rating', models.IntegerField(default=0)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_club.director')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=425)),
                ('rating', models.IntegerField(default=1)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_club.movie')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
