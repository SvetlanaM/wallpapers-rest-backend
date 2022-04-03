from .models import Contact
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'email',
            'phone_number',
            'subject',
            'body',
        ]
