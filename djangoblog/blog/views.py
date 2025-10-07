from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.dates import YearArchiveView

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.select_related('author', 'author__profile')

class PostCreateView(UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class YearArchiveView(YearArchiveView):
    model = Post
    date_field = "created_at"
    make_object_list = True
    template_name = 'blog/year_archive.html'
    context_object_name = 'posts'
    allow_future = True