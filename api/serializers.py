from rest_framework import serializers
from core.models import Meme, Tag


class MemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meme
        fields = ['download_count', 'impression_count', 'view_count',
                  'content', 'tags_list']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
