from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects
    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/home.html', context)