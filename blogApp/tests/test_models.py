from django.test import TestCase
from django.contrib.auth import get_user_model

from blogApp.models import BlogPost, Comment

User = get_user_model()

class BlogPostModelTest(TestCase):
  """Test case for the BlogPost model."""
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    test_user = User.objects.create_user(username='test_user', password='some_password')
    BlogPost.objects.create(title='Hello world', content='How are you doing today?', author=test_user)

  def test_title_label(self):
    blog = BlogPost.objects.get(id=1)
    field_label = blog._meta.get_field('title').verbose_name
    self.assertEqual(field_label, 'title')
  
  def test_content_label(self):
    blog = BlogPost.objects.get(id=1)
    field_label = blog._meta.get_field('content').verbose_name
    self.assertEqual(field_label, 'content')

  def test_post_date_label(self):
    blog = BlogPost.objects.get(id=1)
    field_label = blog._meta.get_field('post_date').verbose_name
    self.assertEqual(field_label, 'post date')
  
  def test_author_label(self):
    blog = BlogPost.objects.get(id=1)
    field_label = blog._meta.get_field('author').verbose_name
    self.assertEqual(field_label, 'author')

  def test_title_max_length(self):
    blog = BlogPost.objects.get(id=1)
    max_length = blog._meta.get_field('title').max_length
    self.assertEqual(max_length, 200)
  
  def test_content_max_length(self):
    blog = BlogPost.objects.get(id=1)
    max_length = blog._meta.get_field('content').max_length
    self.assertEqual(max_length, 1000)

  def test_object_name_is_title(self):
    blog = BlogPost.objects.get(id=1)
    expected_object_name = blog.title
    self.assertEqual(str(blog), expected_object_name)

  def test_get_absolute_url(self):
    blog = BlogPost.objects.get(id=1)
    # This will also fail if the urlconf is not defined.
    self.assertEqual(blog.get_absolute_url(), '/blogApp/blog/1')


class CommentModelTest(TestCase):
  """Test case for the Comment model."""
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    test_user = User.objects.create_user(username='test_user', password='some_password')
    blog = BlogPost.objects.create(title='Hello world', content='How are you doing today?', author=test_user)

    Comment.objects.create(post=blog, description='Is this all you got?', author=test_user)
  
  def test_post_label(self):
    comment = Comment.objects.get(id=1)
    field_label = comment._meta.get_field('post').verbose_name
    self.assertEqual(field_label, 'post')
  
  def test_description_label(self):
    comment = Comment.objects.get(id=1)
    field_label = comment._meta.get_field('description').verbose_name
    self.assertEqual(field_label, 'description')

  def test_comment_date_label(self):
    comment = Comment.objects.get(id=1)
    field_label = comment._meta.get_field('comment_date').verbose_name
    self.assertEqual(field_label, 'comment date')
  
  def test_author_label(self):
    comment = Comment.objects.get(id=1)
    field_label = comment._meta.get_field('author').verbose_name
    self.assertEqual(field_label, 'author')

  def test_description_max_length(self):
    comment = Comment.objects.get(id=1)
    max_length = comment._meta.get_field('description').max_length
    self.assertEqual(max_length, 500)

  def test_object_name_is_description(self):
    comment = Comment.objects.get(id=1)
    expected_object_name = comment.description
    self.assertEqual(str(comment), expected_object_name)

  
  def test_get_absolute_url(self):
    pass
    # comment = Comment.objects.get(id=1)
    # This will also fail if the urlconf is not defined.
    # self.assertEqual(comment.get_absolute_url(), '/blogApp/blog/1/comment')