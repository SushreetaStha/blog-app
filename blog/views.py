from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Blog
from django.urls import reverse_lazy
from . import forms

class BlogList(ListView):
    model= Blog
    template_name='blog/home.html'
    # queryset=Blog.objects.all().order_by('-created_at')
    paginate_by=2

class BlogCreate(CreateView):
    model=Blog
    form_class=forms.BlogForm
    template_name='blog/create.html'
    success_url=reverse_lazy('home')

class BlogUpdate(UpdateView):
    model=Blog
    form_class=forms.BlogForm
    template_name='blog/edit.html'
    success_url=reverse_lazy('home')

class BlogDelete(DeleteView):
    model=Blog
    template_name='blog/delete.html'
    success_url=reverse_lazy('home')



