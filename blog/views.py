from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post_blog
# Create your views here.


def frontblog (request):
    blog_content=post_blog.objects
    return render (request, 'blog/frontblog.html', {'data':blog_content})

def detail (request, detail_id):
    blog_detail = get_object_or_404(post_blog, pk=detail_id)
    return render(request, 'blog/detail.html', {"detail_data":blog_detail})



