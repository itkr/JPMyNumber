from .JPMyNumber import JPMyNumber
from .exceptions import (
    JPMyNumberCheckDigitError,
    JPMyNumberLengthError,
)


def validate_length(number):
    if not JPMyNumber(number).validate_length():
        raise JPMyNumberLengthError


def validate_check_digit(number):
    if not JPMyNumber(number).validate_check_digit():
        raise JPMyNumberCheckDigitError


def validate(number):
    validate_length(number)
    validate_check_digit(number)
