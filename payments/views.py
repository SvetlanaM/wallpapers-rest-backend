from django.shortcuts import render
from django.core.urlresolvers import reverse
from .serializers import InAppSerializer
from .models import InApp
from rest_framework import generics,  permissions
class InAppCreateAPIView(generics.CreateAPIView):
    serializer_class = InAppSerializer
    queryset = InApp.objects.all()

    
