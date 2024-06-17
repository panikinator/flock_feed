from django.shortcuts import render
from django.utils.html import escape
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .helpers import generate_tags
import markdown

# Create your views here.
def homepage(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "flock_feed/index.html", context)

def about_page(request):
    return render(request, "flock_feed/about.html")

class PostListView(ListView):
    model = Post
    template_name = 'flock_feed/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created']

class PostDetailView(DetailView):
    model = Post
class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.tags = generate_tags(form.instance.content)

        form.instance.content = escape(form.instance.content)
        return super().form_valid(form)
