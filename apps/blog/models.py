from django.db import models
from django.utils.text import  slugify
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=100)
    main_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True, help_text='A brief summary of the blog post')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, default=None, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

            counter = 1
            original_slug = self.slug

            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title