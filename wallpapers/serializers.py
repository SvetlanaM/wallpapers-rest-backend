from .models import Wallpaper
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse

class WallpaperSerializer(serializers.HyperlinkedModelSerializer):
    image_thumb = serializers.SerializerMethodField()
    
    def image_thumb(self):
        return "%s%s%s" %('image/upload/w_100,h_100,c_fill,g_face,r_max/', self.image, '.png')   
    class Meta:
        model = Wallpaper
        fields = [
            'id',
            'title',
            'create_url',
        ]
        