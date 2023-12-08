# Standard Library
import re
from typing import List

# Third Party Library
from django import template

register = template.Library()


@register.filter
def split_new_line(value: str) -> List[str]:
    return re.split("\r?\n", value)
