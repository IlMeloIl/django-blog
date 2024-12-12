from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from apps.blog.models import BlogPost, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from apps.blog.forms import BlogPostForm, CommentForm
from django.db.models import Q
from django.core.paginator import Paginator

def paginate(query_set, request, per_page=5):
    paginator = Paginator(query_set, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return page_obj

# Create your views here.
def index(request): 
    blog_posts = BlogPost.objects.filter(status='published')
    page_obj = paginate(blog_posts, request)
    return render(request, 'blog/index.html', {
        'blog_posts': page_obj,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        })   

def post(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.status != 'published':
        raise Http404('Post not found')

    comment_form = CommentForm()
    comments = blog_post.comments.all()
    page_obj = paginate(comments, request)
    
    get_copy = request.GET.copy()
    if 'page' in get_copy:
        get_copy.pop('page')
    query_string = get_copy.urlencode()

    return render(request, 'blog/post.html', {
        'blog_post': blog_post,
        'comment_form': comment_form,
        'comments': page_obj,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'query_string': query_string,
    })

@login_required
@staff_member_required(login_url='index')
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
@staff_member_required(login_url='index')
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

@login_required
@staff_member_required(login_url='index')
def delete_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('index')
    else:
        return redirect('post', slug=slug)

def search(request):
    posts = BlogPost.objects.filter(status='published')

    if "search" in request.GET:
        name_to_search = request.GET['search']
        if name_to_search:
            posts = posts.filter(Q(title__icontains=name_to_search) | Q(main_content__icontains=name_to_search))
    page_obj = paginate(posts, request)

    get_copy = request.GET.copy()
    if 'page' in get_copy:
        get_copy.pop('page')
    query_string = get_copy.urlencode()

    return render(request, 'blog/index.html', {
        'blog_posts': page_obj,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'query_string': query_string,
        })

@login_required
def comment(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post', slug=slug)
        
    return redirect('post', slug=slug)

@login_required
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.user != comment.author:
        return redirect('post', slug=comment.post.slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
            return redirect('post', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.user != comment.author:
        return redirect('post', slug=comment.post.slug)
    
    if request.method == 'POST':
        post_slug = comment.post.slug
        comment.delete()
        return redirect('post', slug=post_slug)
    
    return redirect('post', comment.post.slug)