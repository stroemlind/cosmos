from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('add_post/', views.AddPost.as_view(), name='add-post'),
    path('post/edit/<int:pk>', views.EditPost.as_view(), name='edit-post'),
    path('post/<int:pk>delete/', views.DeletePost.as_view(), name='delete-post'),
]
