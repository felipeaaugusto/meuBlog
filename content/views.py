from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    for post in posts:
        user = User.objects.get(id=post.added_by_id)
        post.first_name = user.first_name
    return render(request, 'home.html',{'posts': posts})
