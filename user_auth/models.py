from django.db import models
from django.contrib.auth.models import AbstractUser
from prose.models import Document

# Create your models here.
class Custom_User(AbstractUser):
    gender_choices=[
        ('m', 'Male'),
        ('f', 'Female'),
        ('u', 'Undefined'),
        ]
    avatar = models.ImageField(upload_to='blog/user/avatar', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=gender_choices, default='u', max_length=1)
    Skills = models.TextField(blank=True, null=True)
    Social_links = models.OneToOneField(Document, on_delete=models.CASCADE, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)

    class Meta:
       verbose_name = 'User'
       verbose_name_plural = 'Users'
    
    def save(self, *args, **kwargs):
        if not self.avatar:
            if self.gender == 'm':
                self.avatar = 'default_avatar_man.png'
            elif self.gender == 'f':
                self.avatar = 'default_avatar_woman.png'
            # else:
            #     self.avatar = 'default_avatar_man.png'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
