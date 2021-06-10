from rest_framework import serializers
from rest_framework import viewsets

from core.models import Meme


class MemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meme
        fields = ['download_count', 'impression_count', 'view_count', 'content',
                  'get_tags']


class MemeView(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    http_method_names = ['head', 'get']
