from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get URL for specific ID/post
from django.conf import settings

# Create your models here.

class BlogPost(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField(
    max_length=1000, help_text="Enter the content of your post"
  )
  post_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

  class Meta:
    ordering = ['post_date']

  def __str__(self) -> str:
    """String for representing the Model object."""
    return self.title
  
  def get_absolute_url(self) -> str:
    """Return the URL to access a detail record for this post."""
    return reverse('blog-post-detail', args=[str(self.id)])


class Comment(models.Model):
  post = models.ForeignKey(BlogPost, on_delete=models.RESTRICT)
  description = models.TextField(max_length=500, help_text="Enter your comment here")
  comment_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

  
  class Meta:
    ordering = ['-comment_date']
  
  def __str__(self) -> str:
    return self.description
  
  '''
    def get_absolute_url(self) -> str:
      """Return the URL to access a detail record for this comment"""
      return reverse('comment-detail', args=[str(self.id)])
  
  '''