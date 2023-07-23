from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("post/<slug:post>/", views.post_single, name="post_single"),
    path("tag/<str:tag>/", views.PostTag.as_view(), name="post_tag"),
    
]
