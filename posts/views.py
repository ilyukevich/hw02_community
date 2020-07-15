#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})


def index_wrong(request):
        latest = Post.objects.order_by("-pub_date")[:11]
        render(request, "index.html", {"posts": latest})


def index_ok(request):
        latest = Post.objects.order_by("-pub_date")[:11]
        response = render(request, "index.html", {"posts": latest})
        return response


def index_ok_too(request):
        latest = Post.objects.order_by("-pub_date")[:11]
        return render(request, "index.html", {"posts": latest})

def group_posts(request, slug):
    """view function for community page"""
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})