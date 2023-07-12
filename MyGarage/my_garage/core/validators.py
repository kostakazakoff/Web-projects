import datetime
from my_garage.core.utils import mbytes_to_bytes
from django.core.exceptions import ValidationError
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.utils import timezone


def validate_img_size_up_to_1mb(image):
    filesize = image.file.size
    max_limit = 1
    if filesize > mbytes_to_bytes(max_limit):
        raise ValidationError(f'Max file size is {max_limit}MB')


def value_is_17_chars(value):
    if len(value) != 17:
        raise ValidationError('VIN code must be exactly 17 characters long!')


def year_is_valid(value):
    if len(value) != 4 or not value.isdigit():
        raise ValidationError('Year must be exactly 4 digit long!')


def validate_url(value):
    validate = URLValidator()
    valid_url = validate(value)
    if not valid_url:
        raise ValidationError('Invalid URL')

#TODO:
def validate_max_date(value):
    max_value = timezone.localdate(timezone.now())
    if value > max_value:
        raise ValidationError("Invalid date of purchase. It can't be after current date")