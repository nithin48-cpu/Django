from django.shortcuts import render, get_object_or_404
from app.models import Post


def allpost(request):
    post = Post.objects
    return render(request, 'post.html', {'post': post})


def details(request, blog_id):
    detail = get_object_or_404(Post, pk=blog_id)
    return render(request, 'details.html', {'post': detail})
