from django.urls import path

from .views import MemeView, TagMemeView, TagView


urlpatterns = [
    path(r'memes', MemeView.as_view()),
    path(r'tags', TagView.as_view()),
    path(r'tags/<tag_name>/memes', TagMemeView.as_view()),
]
