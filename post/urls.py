from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.PostList.as_view(), name='index'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]