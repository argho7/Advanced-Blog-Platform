from django.core.mail import send_mail
from django.conf import settings
import random
import string
from django.template.loader import render_to_string

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

def send_otp_email(request, email, otp):
    verification_link = request.build_absolute_uri(
        f'/verify-email/{email}/{otp}'
    )

    message = render_to_string('emails/email_otp_verification.txt', {
        'username': request.user,
        'otp_code': otp,
        'verification_link': verification_link,
        'email': email,
    })

    subject='Verify Your Email - AdvancedBlogPlatform OTP'
    
    send_email(email, subject, message)