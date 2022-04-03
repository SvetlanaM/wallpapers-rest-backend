from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail
import sendgrid
import os
from sendgrid.helpers.mail import *

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length = 50, blank = True, null = True, default = 'No phone number')
    subject = models.CharField(max_length = 255, blank = True, null = True, default = 'No subject')
    body = models.TextField(blank = True, null = True, default = '\n')
    created_date = models.DateTimeField(auto_now = True, auto_now_add=False)
    updated_date = models.DateTimeField(auto_now= False, auto_now_add = True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def send_contact_email(instance, **kwargs):
        if instance.body is '':
            instance.body = '\n'
        if instance.subject is '':
            instance.subject = 'No subject'
        if instance.phone_number is '':
            instance.phone_number = 'Not filled'

        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email(instance.email)
        subject = instance.subject if not '' else 'No subject'
        to_email = Email("app@wallpaperapp.uk")
        content = Content("text/plain", instance.body + "\n\nPhone number: " + instance.phone_number)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
    post_save.connect(send_contact_email, sender=Contact)
