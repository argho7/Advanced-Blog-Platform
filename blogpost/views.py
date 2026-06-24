from django.shortcuts import render, redirect
from .models import Post, Category, Tags
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context={'posts': Post.objects.all().order_by('-created_at')}
    return render(request, 'home.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
        else:
            context = {
            'categories': Category.objects.all(),
            'tags': Tags.objects.all(),
            'edit_mode': False,
            'form': form,
            }
            messages.error(request, form.errors)
            return render(request, 'create_post.html', context)
    else:
        form = PostForm()
        context = {
            'form': form,
            'categories': Category.objects.all(),
            'tags': Tags.objects.all(),
            'edit_mode': False,
        }
        return render(request, 'create_post.html', context)
