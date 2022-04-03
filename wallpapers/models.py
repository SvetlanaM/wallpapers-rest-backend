from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
class Wallpaper(models.Model):
    title = models.CharField(max_length = 255, blank = True, null = True)
    created_date = models.DateTimeField(auto_now = True, auto_now_add=False)
    updated_date = models.DateTimeField(auto_now= False, auto_now_add = True)
    is_active = models.BooleanField(default = True)
    is_free = models.BooleanField(default = False)
    image = CloudinaryField('Wallpaper', blank = True, null = True)
    class Meta:
        verbose_name = 'Wallpaper'
        verbose_name_plural = 'Wallpapers'

    def __str__(self):
        return "%s" %(self.title)
        
    @property
    def create_url(self, *args, **kwargs):
        if self.image:
            return os.environ('BASE_URL') % (self.image)

    def image_thumb(self):
        return '<img src="" width="100" />' % (self.image)
    image_thumb.allow_tags = True
