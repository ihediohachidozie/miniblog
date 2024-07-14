from django.urls import path
from . import views

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('blog/blogs/', views.BlogPostListView.as_view(), name='blogs'),
  path('blog/<int:pk>', views.BlogPostDetailView.as_view(), name='blog-post-detail'),
  path('blog/<int:pk>/comment/', views.CommentCreateView.as_view(), name='new-blog-comment'),
  path('blog/bloggers', views.BloggersListView.as_view(), name='bloggers'),
  path('blog/blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
  #path('', views.index, name='index'),
  #path('blog/bloggers', views.all_bloggers, name='bloggers'),
  #path('blog/<int:pk>/comment/', views.add_comment, name='new-blog-comment'),
  #path('blog/blogger/<int:pk>', views.blogger_details, name='blogger-detail'),

]