from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Tags
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home(request):
    context={'posts': Post.objects.all().order_by('-created_at')}
    return render(request, 'home.html', context)

@login_required
def post_create(request):
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

def post_view(request, slug):
    context={'post': get_object_or_404(Post, slug=slug)}
    return render(request, 'view_post.html', context)

def search(request):
    query = request.GET.get('q', '')
    type = request.GET.get('type', 'all')
    posts = []
    
    if query:
        if type == 'all':
            posts = Post.objects.filter(Q(title__icontains=query) |
                                        Q(content__icontains=query) |
                                        Q(author__username__icontains=query) |
                                        Q(category__name__icontains=query) |
                                        Q(tags__name__icontains=query)).distinct()
        elif type == 'title':
            posts = Post.objects.filter(Q(title__icontains=query))
        elif type == 'content':
            posts = Post.objects.filter(Q(content__icontains=query))
        elif type == 'author':
            posts = Post.objects.filter(Q(author__username__icontains=query))
        elif type == 'category':
            posts = Post.objects.filter(Q(category__name__icontains=query))
        elif type == 'tag':
            posts = Post.objects.filter(Q(tags__name__icontains=query))
        
        if request.user.is_superuser:
            posts=posts.order_by('-created_at')
        else:
            posts=posts.filter(status='published', visibility='public').order_by('-created_at')

    context={'posts':posts, 'query': query}
    return render(request, 'search.html', context)