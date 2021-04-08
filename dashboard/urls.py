from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('post/', views.CreatePostView.as_view(), name='post'),
    path('view_post/', views.PostView.as_view(), name='view_post'),
    path('delete_post/delete/<int:pk>',views.DeletePost.as_view(),name='delete_post'),
    path('update_post/<int:pk>',views.UpdatePost.as_view(),name='update_post'),
    path('detail_post/<slug:slug>',views.DetailPost.as_view(),name='detail_post'),

    path('Comment_view',views.CommentView.as_view(),name='comment_view')

]