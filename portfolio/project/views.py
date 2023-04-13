from django.shortcuts import render

from project.models import Project
# Create your views here.

def index(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'project/index.html', context)