# Third Party Library
from candidate.models import Candidate


def get_candidate():
    return Candidate.objects.all().first()


def get_education_certificate_url(pk):
    candidate = get_candidate()
    url = candidate.educations.get(pk=pk).image.url
    return url
