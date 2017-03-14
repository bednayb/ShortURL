import random
import string

from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 8)


# create a shortcode generator (any string or digit, 8 character)
def shortcode_generator(size = SHORTCODE_MIN, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def create_shortcode(instance, size = SHORTCODE_MIN):
    new_code = shortcode_generator(size = size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode= new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
