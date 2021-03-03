from django import forms
from .models import Post, Category

category_choices = Category.objects.all().values_list('name','name')
category_list = []

for category in category_choices:
    category_list.append(category)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippit')

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title for webpage tab'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = category_choices, attrs={'class': 'form-control capitalise'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippit': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Snippit for displaying on the index page..'}),

        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippit')

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title for webpage tab'}),
            'category': forms.Select(choices = category_choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippit': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Snippit for displaying on the index page..'}),

        }