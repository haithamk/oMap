from map_info.models import Point, Layer
from django.contrib.gis import admin

class LayerAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'owner',)


class PointAdmin(admin.OSMGeoAdmin):
    list_display = ('subject', 'date_added', 'user', 'layer',)
    list_display_links = ('subject',)
    list_editable = ('layer',)
    list_filter = ('layer__name',)
    search_fields = ('user__username',)
    ordering = ['-date_added']

admin.site.register(Layer, LayerAdmin)
admin.site.register(Point, PointAdmin)