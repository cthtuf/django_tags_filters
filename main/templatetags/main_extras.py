from django import template
from hashlib import (sha1, md5)
import random
import string


register = template.Library()


@register.filter(name='get_hash')
def get_hash(value, arg):
    if arg == 'sha1':
        hash = sha1(value.encode('utf-8'))
    elif arg == 'md5':
        hash = md5(value.encode('utf-8'))
    else:
        hash = None
        return 'Error: Wrong hash method'

    return hash.hexdigest()


@register.simple_tag
def get_random_string(length):
    return ''.join([random.choice(string.ascii_lowercase) for i in range(length)])

