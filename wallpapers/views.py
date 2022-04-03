from django.shortcuts import render
from django.core.urlresolvers import reverse
from .serializers import WallpaperSerializer
from .models import Wallpaper
from rest_framework import generics,  permissions
from rest_framework.response import Response
from rest_framework import status
class WallpaperListAPIView(generics.ListAPIView):
    serializer_class = WallpaperSerializer

    def get_queryset(self):
        queryset = Wallpaper.objects.filter(is_active = True)
        is_free = self.request.query_params.get('is_free', None)
        try:
            if is_free is not None:
                is_free = is_free.title()
                queryset = queryset.filter(is_free=is_free)
            return queryset
        except:
            pass
