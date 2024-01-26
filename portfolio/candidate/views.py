# Third Party Library
from candidate.services import (
    get_candidate,
    get_education_certificate_url,
    get_client_ip,
)
from django.http import JsonResponse
from django.shortcuts import render
from candidate.models import Ip

# Create your views here.


def index(request):
    ip = get_client_ip(request)
    Ip.objects.create(ip=ip, candidate=get_candidate())

    context = {
        "candidate": get_candidate,
    }
    return render(request, "project/index.html", context)


def render_education_certificate(request):
    certificate_id = request.GET.get("pk", None)
    return JsonResponse({"url": get_education_certificate_url(certificate_id)})
