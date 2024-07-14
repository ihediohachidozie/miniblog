from django.contrib import admin
from .models import BlogPost, Comment



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'post_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('post', 'description', 'author', 'comment_date')

# Register your models here.
#admin.site.register(BlogPost)
#admin.site.register(Comment)