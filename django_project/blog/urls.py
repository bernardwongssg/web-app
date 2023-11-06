from django.urls import path
from . import views 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    #path('', views.home, name = 'blog-home'),
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'), # pk is passed in so we know which post we're updating
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'), # pk is passed in so we know which post we're deleting
    path('about/', views.about, name = 'blog-about'),
]
