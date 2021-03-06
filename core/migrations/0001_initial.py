# Generated by Django 3.2.4 on 2021-06-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('download_count', models.IntegerField()),
                ('impression_count', models.IntegerField()),
                ('content', models.FileField(upload_to='content')),
                ('view_count', models.IntegerField()),
                ('tags', models.ManyToManyField(related_name='memes', to='core.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
