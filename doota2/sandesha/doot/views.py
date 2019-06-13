from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def HomeView(request):
    queryset = Post.objects.all()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    context = {
        'postlist' : queryset,
        'form': form
    }
    return render(request, 'doot/home.html', context)