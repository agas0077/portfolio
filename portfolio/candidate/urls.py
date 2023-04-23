from django.urls import path

from candidate.views import index

app_name = 'candidate'

urlpatterns = [
    path('', index),
]
