from django.db import models
import datetime
from .utils import shortcode_generator, create_shortcode
# Create your models here.



class BenURLManager(models.Manager):
    def all(self, *args, **keyword_args):
        query_set = super(BenURLManager, self).all(*args, **keyword_args)
        query_set = query_set.filter(active = True)
        return query_set

class BenURL(models.Model):
    url = models.CharField(max_length=200, )
    # every shortcode should be unique
    shortcode = models.CharField(max_length=15, unique=True, blank= True)
    #  when was the model modified last time
    created_datetime = models.DateTimeField(auto_now = True)
    # when was the model created
    update_timestamp = models.DateTimeField(auto_now_add = True)
    # show if an element active
    active = models.BooleanField(default = True)

    # refresh how many element is active
    objects = BenURLManager()

    def save(self, *args, **keyword_args):
        # create shortcode if the url doesnt have it
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(BenURL, self).save(*args, **keyword_args)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return set(self.url)
