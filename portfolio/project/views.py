from django.shortcuts import render

from candidate.models import Candidate
# Create your views here.


def index(request):
    context = {
        'candidate': Candidate.objects.all().first(),
    }
    return render(request, 'project/index.html', context)
