from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request,'dashboard/index.html')


def create_post(request):
    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.author = request.user
            data.save()
            return HttpResponse('done')
    else:
        form = PostForm()
        return render(request,'dashboard/create_post.html',{'form':form})
