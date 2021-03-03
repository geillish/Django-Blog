from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, UpdateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class HomeView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'