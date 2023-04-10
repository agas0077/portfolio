from django.urls import path, include

from project.views import index

app_name = 'project'

urlpatterns = [
    path('', index),
]