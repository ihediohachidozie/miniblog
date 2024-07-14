from django.contrib.auth.decorators import login_required
from django.forms import BaseModelForm
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy


from blogApp.forms import AddCommentModelForm
from .models import BlogPost, Comment
# Create your views here.

# Class Based Views

class HomeView(generic.TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    User = get_user_model()

    context['num_posts'] = BlogPost.objects.count()
    context['num_users'] = User.objects.count()
    context['num_comments'] = Comment.objects.count()

    #context['bloglists'] = BlogPost.objects.filter(author=self.kwargs['pk'])

    return context


class BlogPostListView(generic.ListView):
  model = BlogPost
  context_object_name = 'blogpost_list' # template variable name

  def get_queryset(self):
    return BlogPost.objects.all() # Get all post
  
  template_name = 'blogpost_list.html'
  paginate_by = 10


class BlogPostDetailView(generic.DetailView):
  model = BlogPost
  template_name = 'blogpost_detail.html'


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
 # Create a new comment
  model = Comment
  fields = ["description"]
  template_name = 'add_comment.html'
  

  def form_valid(self, form: BaseModelForm) -> HttpResponse:
    """
      Add author and associated blog to form data before setting it as valid
      (so it is saved to model)
    """
    # Add logged-in user as author of comment
    form.instance.author = self.request.user
    # Associate comment with blog based on passed id
    form.instance.post=get_object_or_404(BlogPost, pk = self.kwargs['pk'])
    return super().form_valid(form)
  
  # overriding the get_success_url 
  def get_success_url(self):
    # Redirect back to the post details
    return reverse('blog-post-detail', args=(self.kwargs['pk'],))


class BloggersListView(generic.ListView):
  User = get_user_model()
  model = User
  context_object_name = 'bloggers'
  template_name = 'bloggers_list.html'
  paginate_by = 10

  def get_queryset(self):
    return self.User.objects.all() # Get all post
  

class BloggerDetailView(generic.DetailView):
  blogger = get_user_model()
  model = blogger
  template_name = 'blogger_details.html'
  context_object_name = 'blogger'


  def get_context_data(self, **kwargs):
    
    context = super().get_context_data(**kwargs)

    context['bloglists'] = BlogPost.objects.filter(author=self.kwargs['pk'])

    return context

"""

  # function based views

  def index(request):
    
    '''View function for home page of site.'''

    # Generate counts of some main objects.
    num_posts = BlogPost.objects.count()
    User = get_user_model()
    num_users = User.objects.count()
    num_comments = Comment.objects.count()

    context = {
      'num_posts': num_posts,
      'num_users': num_users,
      'num_comments': num_comments
    }

    return render(request, 'index.html', context)


  @login_required
  def add_comment(request, pk):
    '''View function for adding a post comment by author.
    post = get_object_or_404(BlogPost, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

      # Create a form instance and populate it with data from the request (binding):
      form = AddCommentModelForm(request.POST)

      # Check if the form is valid:
      if form.is_valid():
        # process the data in form.cleaned_data as required (here we just write it to the model description field)
        description = form.cleaned_data['description']
        comment = Comment.objects.create(
          post=post, description=description, author=request.user
        )
        

      return HttpResponseRedirect(reverse('blog-post-detail', args=(post.id,)))
    # If this is a GET (or any other method) create the default form.
    else:
      form = AddCommentModelForm()
      context = {
        'form': form,
        'post': post,
      }
    
    return render(request, 'add_comment.html', context)


  def all_bloggers(request):
    User = get_user_model()
    bloggers = User.objects.all()

    context = {
      'bloggers': bloggers
    }
    return render(request, 'allbloggers.html', context)


  def blogger_details(request, pk):
    User = get_user_model()
    blogger = User.objects.get(pk=pk)
    blogslist = BlogPost.objects.filter(author=blogger.id)

    context = {
      'blogger' : blogger,
      'blogslist': blogslist
    }
    return render(request, 'blogger_details.html', context)

"""

