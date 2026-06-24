from django import forms
from tinymce.widgets import TinyMCE
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 5}))
    
    class Meta:
        model = Post
        fields = ['title', 'thumbnail', 'category', 'tags',
                   'status', 'visibility', 'content']