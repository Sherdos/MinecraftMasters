from django.urls import path
from posts.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('news/<int:pk>/', PostDetailView.as_view(), name='new_detail'),
]