# Third Party Library
from candidate.views import index, render_education_certificate
from django.urls import path

app_name = "candidate"

urlpatterns = [
    path("", index, name="index"),
    path(
        "candidate/certificate",
        render_education_certificate,
        name="certificate",
    ),
]
