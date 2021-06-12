import uuid

from django.db import models

from .constants import EMPTY_COUNT


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    uid = models.CharField(max_length=128, default=uuid.uuid4)

    class Meta:
        abstract = True


class Meme(BaseModel):
    download_count = models.IntegerField(default=EMPTY_COUNT)
    impression_count = models.IntegerField(default=EMPTY_COUNT)
    content = models.FileField(upload_to='content')
    tags = models.ManyToManyField(
        'core.Tag',
        blank=False,
        related_name='memes'
    )
    view_count = models.IntegerField(default=EMPTY_COUNT)

    def tags_list(self):
        return ', '.join([t.name for t in self.tags.all()])


class Tag(BaseModel):
    name = models.CharField(max_length=128)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
