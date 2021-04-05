from django.views import generic
from .models import Post,Contact
from .forms import CommentForm, ContactForm
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q') # new
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) 
        )
        return object_list


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'



class Contact(SuccessMessageMixin,generic.CreateView):
    form_class = ContactForm
    model = Contact
    template_name = "contact.html"
    success_url ="/contact"
    success_message = "Contact was submitted successfully"

