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

    #Need to finish this so I can have it as a global function for all views so the code doesn't become wet.
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

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
    category_posts = Post.objects.filter(category=category.replace('-', ' '))
    category_paginator = Paginator(category_posts, 5)

    page_num = request.GET.get('page')
    page = category_paginator.get_page(page_num)
    
    return render(request, 'categories.html', {'page':page, 'category':category.title().replace('-',' '), 'category_posts':category_posts})

def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'category_menu_list':category_menu_list})