# Standard Library
from typing import Any

# Third Party Library
from candidate.models import Candidate
from candidate.services import get_candidate, get_education_certificate_url
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


def index(request):
    context = {
        "candidate": get_candidate,
    }
    return render(request, "project/index.html", context)


def render_education_certificate(request):
    certificate_id = request.GET.get("pk", None)
    return JsonResponse({"url": get_education_certificate_url(certificate_id)})
