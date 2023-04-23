from django.shortcuts import render

from candidate.models import Candidate
# Create your views here.


def index(request):
    print(Candidate.objects.all())
    context = {
        'candidate': Candidate.objects.all().first(),
    }
    return render(request, 'project/index.html', context)
