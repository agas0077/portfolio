# Third Party Library
from candidate.views import index
from django.urls import path

app_name = "candidate"

urlpatterns = [
    path("", index),
]
