from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('post/', views.CreatePostView.as_view(), name='post'),
    path('view_post/', views.PostView.as_view(), name='view_post'),
]