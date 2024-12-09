from django.http import Http404
from django.shortcuts import render, get_object_or_404
from apps.blog.models import BlogPost

# Create your views here.
def index(request): 
    blog_posts = BlogPost.objects.filter(status='published')
    return render(request, 'blog/index.html', {'blog_posts': blog_posts})

def post(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.status != 'published':
        raise Http404('Post not found')

    return render(request, 'blog/post.html', {'blog_post': blog_post})
