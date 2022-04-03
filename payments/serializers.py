from .models import InApp
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
class InAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InApp
        fields = [
            'id',
            'shop',
            'shop_price',
            'currency',
        ]
