from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from apps.blog.models import BlogPost
from django.contrib.auth.decorators import login_required
from apps.blog.forms import BlogPostForm

# Create your views here.
def index(request): 
    blog_posts = BlogPost.objects.filter(status='published')
    return render(request, 'blog/index.html', {'blog_posts': blog_posts})

def post(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.status != 'published':
        raise Http404('Post not found')

    return render(request, 'blog/post.html', {'blog_post': blog_post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form,  'post': post})
