from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,)
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=50,)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    status_choices=[
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('scheduled', 'Scheduled'),
        ('archived', 'Archived'),
    ]
    visiblity_choices=[
        ('public', 'Public'),
        ('private', 'Private'),
        ('followers_only', 'Followers_only'),
        ]
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='blog/post/thumbnails/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    from prose.fields import RichTextField
    pr=RichTextField(blank=True, null=True)

    from tinymce.models import HTMLField
    mc=HTMLField(blank=True, null=True)

    category = models.ForeignKey(Category, default='uncategorized', on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tags, blank=True)
    status=models.CharField(max_length=9, choices=status_choices, default='draft')
    visiblity = models.CharField(max_length=14, choices=visiblity_choices, default='private')
    def __str__(self):
        return self.title
    