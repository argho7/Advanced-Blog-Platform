from django.urls import path
from .views import user_login, user_registration, verify_email

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_registration, name='register'),
    path('verify-email/', verify_email, name='verify_email'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify_email'),
]
