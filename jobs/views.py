from django.shortcuts import render

from .models import Job, Viewer


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})


def viewers(request):
    viewers = Viewer.objects
    return render(request, 'jobs/viewers.html', {'viewers': viewers})
