from my_garage.core.utils import mbytes_to_bytes
from django.core.exceptions import ValidationError


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
