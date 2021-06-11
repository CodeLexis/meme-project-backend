from rest_framework import serializers
from core.models import Meme


class MemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meme
        fields = ['download_count', 'impression_count', 'view_count',
                  'content', 'get_tags']
