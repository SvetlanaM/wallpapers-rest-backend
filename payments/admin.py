from django.contrib import admin
from .models import InApp

class InAppAdmin(admin.ModelAdmin):
    list_display = ('shop', 'created_date', 'shop_price', 'currency')
    list_filter = ('shop', 'created_date')
    list_per_page = 100

admin.site.register(InApp, InAppAdmin)
