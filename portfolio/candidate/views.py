# Third Party Library
from candidate.models import Candidate
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "candidate": Candidate.objects.all().first(),
    }
    return render(request, "project/index.html", context)
