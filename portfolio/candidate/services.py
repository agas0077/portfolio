# Third Party Library
from candidate.models import Candidate


def get_candidate():
    return Candidate.objects.get(is_chosen_candidate=True)


def get_education_certificate_url(pk):
    candidate = get_candidate()
    url = candidate.educations.get(pk=pk).image.url
    return url
