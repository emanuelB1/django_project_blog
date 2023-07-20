from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView

from .models import Post

# Create your views here.


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"
    

def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    related = Post.objects.filter(author=post.author)[:5]
    return render(request, "blog/single.html", {"post": post, "related": related})


class PostTag(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        tag_name = self.kwargs.get("tag")
        return Post.objects.filter(tags__name__iexact=tag_name, status="published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("tag")
        return context

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"
 
    
class SearchView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            title_results = Post.objects.filter(Q(title__icontains=query), status="published")
            content_and_tags_results = Post.objects.filter(
                Q(content__icontains=query) |
                Q(tags__name__icontains=query) |
                Q(author__username__icontains=query),
                status="published"
            )

            # Combine the title results and content/tags results into a list
            results = list(title_results) + list(content_and_tags_results)
            return results

        return Post.objects.none()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q")
        return context

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"

    def get_success_url(self):
        return reverse("homepage")  # Redirige al homepage después de una búsqueda exitosa
    