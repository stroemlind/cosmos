from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>', views.get_post, name='post-detail'),
    # path('add_post/', views.AddPost.as_view(), name='add-post'),
    path('add_post/', views.add_post, name='add-post'),
    path('post/edit/<int:pk>', views.EditPost.as_view(), name='edit-post'),
    path('post/<int:pk>delete/', views.DeletePost.as_view(), name='delete-post'),
    path('category/<str:categories>/', views.category_page, name='category'),
    # path('category/<str:categories>/', views.category_menu, name='category-menu'),
    path('like/<int:pk>', views.LikeView.as_view(), name='post_like'),
    # path('popular_post/', views.PopLikes.as_view(), name='popular_post'),
]
