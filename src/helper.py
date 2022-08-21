import validators
from validators import ValidationFailure


def is_string_url(url_str: str):
    result = validators.url(url_str)
    if isinstance(result, ValidationFailure):
        return False
    return True
