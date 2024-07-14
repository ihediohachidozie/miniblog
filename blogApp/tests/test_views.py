from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blogApp.models import BlogPost, Comment

User = get_user_model()
blogger = User.objects.get(id=1)

class HomeViewTest(TestCase):

  def test_view_url_exists_at_desired_location(self):
    response = self.client.get('/blogApp/')
    self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'index.html')


class BlogPostListViewTest(TestCase):
  def setUp(self):
    # Set up non-modified objects used by all test methods
    test_user = User.objects.create_user(username='test_user', password='some_password')
    for x in range(20):
      BlogPost.objects.create(title=f'Hello world {x}', content=f'How are you doing today {x}?', author=test_user)

  def test_view_url_exists_at_desired_location(self):
    response = self.client.get('/blogApp/blog/blogs/')
    self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
    response = self.client.get(reverse('blogs'))
    self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('blogs'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blogpost_list.html')
  
  def test_pagination_is_ten(self):
    response = self.client.get(reverse('blogs'))
    self.assertEqual(response.status_code, 200)
    self.assertTrue('is_paginated' in response.context)
    self.assertTrue(response.context['is_paginated'] is True)
    self.assertEqual(len(response.context['blogpost_list']), 10)


class BlogPostDetailViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    test_user = User.objects.create_user(username='test_user', password='some_password')
    BlogPost.objects.create(title='Hello world', content='How are you doing today?', author=test_user)

  def test_view_url_accessible_by_name(self):
    blog = BlogPost.objects.get(id=1)
    response = self.client.get(reverse('blog-post-detail', args=(blog.id,)))
    self.assertEqual(response.status_code, 200)
  
  def test_view_uses_correct_template(self):
    blog = BlogPost.objects.get(id=1)
    response = self.client.get(reverse('blog-post-detail', args=(blog.id,)))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blogpost_detail.html')


class BloggersListViewTest(TestCase):
  def test_view_url_exists_at_desired_location(self):
    response = self.client.get('/blogApp/blog/bloggers')
    self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
    response = self.client.get(reverse('bloggers'))
    self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('bloggers'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'bloggers_list.html')


class BloggerDetailViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    test_user = User.objects.create_user(username='test_user', password='some_password')

  def test_view_url_accessible_by_name(self):
    response = self.client.get('/blogApp/blog/blogger/'+ str(blogger.id,))
    self.assertEqual(response.status_code, 200)
  
  def test_view_uses_correct_template(self):  
    response = self.client.get('/blogApp/blog/blogger/'+ str(blogger.id,))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blogger_details.html')


class CommentCreateViewTest(TestCase):
  ...



 