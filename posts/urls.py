from django.urls import path
from .views import PostsList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostsList.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
