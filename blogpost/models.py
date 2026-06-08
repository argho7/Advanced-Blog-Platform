from django.db import models
from .utils import Generate_Slug
from prose.models import Document
from user_auth.models import Custom_User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=50,)
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
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
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Custom_User, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='blog/post/thumbnails/', blank=True, null=True)
    content = models.OneToOneField(Document, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, default='uncategorized', null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, blank=True)
    status=models.CharField(max_length=9, choices=status_choices, default='draft')
    visibility = models.CharField(max_length=14, choices=visiblity_choices, default='private')
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=Generate_Slug(Post, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    