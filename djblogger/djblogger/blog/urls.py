from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("post/<slug:post>/", views.post_single, name="post_single"),
    path("tag/<str:tag>/", views.PostTag.as_view(), name="post_tag"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
]
