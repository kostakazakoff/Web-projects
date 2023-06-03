from my_garage.core.utils import mbytes_to_bytes
from django.core.exceptions import ValidationError

def validate_img_size_up_to_1mb(image):
    filesize = image.file.size
    max_limit = 1
    if filesize > mbytes_to_bytes(max_limit):
        raise ValidationError(f'Max file size is {max_limit}MB')
