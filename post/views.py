from django.views import generic
from .models import Comment, Post,Contact
from .forms import CommentForm, ContactForm
from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

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
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        comments = Comment.objects.filter(
            post=post, parent=None).order_by('-id')

        def post(self, request, *args, **kwargs):
            comment_form = CommentForm(self.request.POST or None)
            if comment_form.is_valid():
                content = self.request.POST.get('content')
                comments=Comment.objects.create(post=post,created_by=self.request.user,content=content)
                return HttpResponseRedirect("post_detail.html")
        
        comment_form = CommentForm()

        context["comments"] = comments
        context["comment_form"] = comment_form
        return context

# class PostCommentCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Comment
#     form_class = CommentForm

#     def form_valid(self, form):
#         post = get_object_or_404(Post, slug=self.kwargs['slug'])
#         form.instance.created_by = self.request.user
#         form.instance.post = post
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         return HttpResponseRedirect(self.get_success_url())

#     def get_success_url(self,re):
#         return reverse('score:post-detail', kwargs=dict(slug=self.kwargs['slug']))

class Contact(SuccessMessageMixin,generic.CreateView):
    form_class = ContactForm
    model = Contact
    template_name = "contact.html"
    success_url ="/contact"
    success_message = "Contact was submitted successfully"

class PlaceFormView(generic.CreateView):
    form_class = CommentForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceFormView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())