from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework import routers
from wallpapers.views import WallpaperListAPIView
from payments.views import InAppCreateAPIView
from rest_framework_swagger.views import get_swagger_view
from emails.views import ContactCreateAPIView

schema_view = get_swagger_view(title='Wallpaper API')

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='admin'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1.0/wallpapers$', WallpaperListAPIView.as_view(), name='get_wallpapers'),
    url(r'^api/v1.0/inapp$', InAppCreateAPIView.as_view(), name='create_inapp'),
    url(r'^api/v1.0/contact$', ContactCreateAPIView.as_view(), name='create_email'),
    url(r'^api/v1.0/docs/$', schema_view),
]
