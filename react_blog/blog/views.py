from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.messages.views import SuccessMessageMixin

from .models import Post
from .forms import PostForm


class PostList(generic.ListView):
    template_name = "blog/blog_index.html"
    context_object_name = "posts"
    queryset = Post.objects.all()


class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post.html"


@method_decorator(login_required, "dispatch")
class PostCreate(SuccessMessageMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"
    success_message = "Post Created successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


@method_decorator(login_required, "dispatch")
class PostEdit(SuccessMessageMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_edit.html"
    success_message = "Post updated successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostEdit, self).form_valid(form)

    def get_object(self, queryset=None):
        obj = get_object_or_404(Post, pk=self.kwargs['pk'])
        if self.request.user == obj.author:
            return obj
        else:
            raise Http404()


class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")
    template_name = 'blog/post_delete.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Post, pk=self.kwargs['pk'])
        if self.request.user == obj.author:
            return obj
        else:
            raise Http404()


class Login(LoginView):
    template_name = 'login.html'


class Logout(LogoutView):
    pass