from map.map_info.models import Point, Layer, Comment
from django.contrib.gis import admin

class LayerAdmin(admin.OSMGeoAdmin):

    """ModelAdmin for the layers"""

    list_display = ('name', 'owner',)


class PointAdmin(admin.OSMGeoAdmin):

    """ModelAdmin for the points."""

    list_display = ('subject', 'date_added', 'user', 'layer',)
    list_display_links = ('subject',)
    list_editable = ('layer',)
    list_filter = ('layer__name',)
    search_fields = ('user__username',)
    ordering = ['-date_added']

class CommentAdmin(admin.ModelAdmin):

    """ModelAdmin for the comments"""

    display_fields = ["point", "author", "created"]

admin.site.register(Layer, LayerAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Comment, CommentAdmin)