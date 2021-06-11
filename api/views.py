from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Meme
from .pagination import StandardResultsSetPagination
from .serializers import MemeSerializer


class MemeView(viewsets.ModelViewSet):
    http_method_names = ['head', 'get']
    queryset = Meme.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = MemeSerializer

    def retrieve(self, request, *args, **kwargs):
        print('AAAAAA', request.params)
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
