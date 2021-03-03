from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'index.html'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

#Showing I can use function based views aswell.
def CategoryView(request, category):
    category_posts = Post.objects.filter(category=category)
    category_paginator = Paginator(category_posts, 5)

    page_num = request.GET.get('page')
    page = category_paginator.get_page(page_num)
    
    return render(request, 'categories.html', {'page':page, 'category':category, 'category_posts':category_posts})