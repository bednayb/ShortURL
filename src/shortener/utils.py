import random
import string

# create a shortcode generator (any string or digit, 8 character)
def shortcode_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def create_shortcode(instance, size = 8):
    new_code = shortcode_generator(size = size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode= new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
