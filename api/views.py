from rest_framework.response import Response
from rest_framework import generics

from core.models import Meme, Tag
from .pagination import StandardResultsSetPagination
from .serializers import MemeSerializer, TagSerializer


class MemeView(generics.ListAPIView):
    queryset = Meme.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = MemeSerializer


class TagMemeView(generics.ListAPIView):
    queryset = Tag.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = MemeSerializer

    def list(self, request, *args, **kwargs):
        tag_name = kwargs['tag_name']

        memes_queryset = Meme.objects.filter(
            tags__name=tag_name
        ).all()

        page = self.paginate_queryset(memes_queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(memes_queryset, many=True)

        return Response(serializer.data)


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = TagSerializer
