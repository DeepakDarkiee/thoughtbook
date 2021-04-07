from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('post/', views.CreatePostView.as_view(), name='post'),
    path('view_post/', views.PostView.as_view(), name='view_post'),
    path('delete_post/<int:pk>',views.DeletePost.as_view(),name='delete_post')
]