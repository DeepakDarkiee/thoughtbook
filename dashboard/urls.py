from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('post/', views.create_post, name='post'),
]