from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('comment/', views.CommentCreateView.as_view(), name='comment'),
]