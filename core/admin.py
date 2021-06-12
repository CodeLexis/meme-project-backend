from django.contrib import admin

from .models import Meme, Tag


class MemeAdmin(admin.ModelAdmin):
    list_display = (
        'date_created', 'download_count', 'impression_count', 'view_count',
        'content', 'tags_list',
    )
    fields = ['content', 'tags']


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'date_created', 'name',
    )
    fields = ['name']


admin.site.register(Meme, MemeAdmin)
admin.site.register(Tag, TagAdmin)
