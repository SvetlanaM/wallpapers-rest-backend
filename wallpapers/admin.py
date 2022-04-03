from django.contrib import admin
from .models import Wallpaper
from django.contrib.auth.models import Group
class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_free', 'image_thumb')
    list_filter = ('created_date', 'is_free')
    list_editable = ('is_free', )
    list_per_page = 100
    
admin.site.register(Wallpaper, WallpaperAdmin)
admin.site.unregister(Group)