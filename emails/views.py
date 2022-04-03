from django.shortcuts import render
from django.core.urlresolvers import reverse
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import generics,  permissions

class ContactCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
