from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/<int:pk>', views.get_post, name='post-detail'),
    path('add_post/', views.add_post, name='add-post'),
    path('post/edit/<int:pk>', views.EditPost.as_view(), name='edit-post'),
    path(
        'post/<int:pk>/delete/',
        views.DeletePost.as_view(),
        name='delete-post'),
    path('category/', views.category_page, name='category'),
    path('like/<int:pk>', views.LikeView.as_view(), name='post_like'),
    path('post/<int:pk>/add-comment/', views.add_comment, name='add-comment'),
    path('popular_post/', views.MostLikedPost.as_view(), name='popular_post'),
]
