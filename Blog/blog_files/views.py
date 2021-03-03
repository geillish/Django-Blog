from django.shortcuts import render
from django.views.generic import ListView, DetailView

class HomeView(ListView):
    model = Post
    template_name = 'index.html'