from django.shortcuts import render
from .models import Post

def post_list(request):

    p=Post.objects.order_by('title')
    return render(request, 'blog/post_list.html', {"post":p})