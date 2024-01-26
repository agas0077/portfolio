# Third Party Library
from candidate.models import Candidate, Ip


def get_candidate():
    """
    Get the chosen candidate.

    Returns:
    Candidate: The chosen candidate object, or None if no candidate is chosen.
    """
    candidate = Candidate.objects.filter(is_chosen_candidate=True)
    if not candidate:
        return
    return candidate[0]


def get_education_certificate_url(pk):
    """
    Get the URL of the education certificate image for a candidate.

    Args:
    pk (int): The primary key of the education certificate.

    Returns:
    str: The URL of the education certificate image.
    """

    candidate = get_candidate()
    url = candidate.educations.get(pk=pk).image.url
    return url


def get_client_ip(request):
    """
    Get the client's IP address from the request.

    Args:
    request (HttpRequest): The HTTP request object.

    Returns:
    str: The client's IP address.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def count_unique_ips():
    """
    Count the number of unique IP addresses in the database.

    Returns:
    int: The count of unique IP addresses.
    """
    return Ip.objects.order_by("ip").values_list("ip").distinct().count()


def count_ips():
    """
    Count the number of IP addresses in the database.

    Returns:
    int: The count of unique IP addresses.
    """
    return Ip.objects.order_by("ip").values_list("ip").count()


def count_chosen_candidate_unique_ips(candidate):
    """
    Count the number of unique IP addresses viewed the chosen candidate.

    Args:
    candidate (Candidate): The chosen candidate object.

    Returns:
    int: The count of unique IP addresses viewed the candidate.
    """
    return (
        Ip.objects.filter(candidate=candidate)
        .order_by("ip")
        .values_list("ip")
        .distinct()
        .count()
    )


def count_chosen_candidate_ips(candidate):
    """
    Count the number of IP addresses viewed the chosen candidate.

    Args:
    candidate (Candidate): The chosen candidate object.

    Returns:
    int: The count of all IP addresses viewed the candidate.
    """
    return (
        Ip.objects.filter(candidate=candidate)
        .values_list("ip")
        .order_by("ip")
        .count()
    )
