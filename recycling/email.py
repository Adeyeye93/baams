# views.py
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def send_email_blast(request, subject, message, recipients):
    subject = subject
    message = message
    recipients = [recipients] 
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # Sender's email address
        recipients,  # List of recipient email addresses
        fail_silently=False,
    )
    print("Email sent")