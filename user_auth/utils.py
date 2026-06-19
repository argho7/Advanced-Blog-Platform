from django.core.mail import send_mail
from django.conf import settings
import random
import string
from django.template.loader import render_to_string
from datetime import date

def send_email(receiver=None, subject=None, message=None):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[receiver],
        fail_silently=False,
    )

def generate_otp():
    """Generate a 6-digit OTP"""
    return ''.join(random.choices(string.digits, k=6))

def send_otp_email(request, username, email, otp):
    verification_link = request.build_absolute_uri(
        '/verify-email/'
    )

    message = render_to_string('emails/email_otp_verification.txt', {
        'username': username,
        'otp_code': otp,
        'verification_link': verification_link,
        'email': email,
        'year' : date.today().year
    })
    subject='Verify Your Email - AdvancedBlogPlatform OTP'
    
    send_email(email, subject, message)