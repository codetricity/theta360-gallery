from django.shortcuts import render, get_object_or_404

from .models import Blog
from jobs.models import Job


def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def qualitytuba(request):
    blogs = Blog.objects
    return render(request, 'blog/quality.html', {'blogs': blogs})


def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    job = Job.objects.get(detail_page=detailblog)
    return render(
        request,
        'blog/detail.html',
        {
            'blog': detailblog,
            'job': job
        })

def quality_detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(
        request,
        'blog/quality_detail.html',
        {
            'blog': detailblog
        })

def about(request):
    return render(request, 'blog/about.html')


def award201905(request):
    return render(request, 'blog/projectaward.html')