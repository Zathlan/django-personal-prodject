from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class PostsList(ListView):
    model = Post
    template_name = "home.html"


class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["item", "owner", "description", "price", "cover"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["item", "description", "price", "cover"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
