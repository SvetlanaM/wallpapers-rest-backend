from django.db import models

SHOP_CHOICES = (
    ('iOS', 'App Store'),
    ('Android', 'Google Play'),
)
class InApp(models.Model):
    created_date = models.DateTimeField(auto_now = True, auto_now_add=False)
    updated_date = models.DateTimeField(auto_now= False, auto_now_add = True)
    is_active = models.BooleanField(default = True)
    shop = models.CharField(max_length = 10, choices = SHOP_CHOICES)
    shop_price = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length = 10, blank = True, null = True)
    class Meta:
        verbose_name = 'InApp purchase'
        verbose_name_plural = 'InApp purchases'

    def __str__(self):
        return "%s_%s" %(self.shop_price, self.currency)
