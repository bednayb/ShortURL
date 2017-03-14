from django.conf import settings
from django.db import models
import datetime
from .utils import shortcode_generator, create_shortcode
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class BenURLManager(models.Manager):
    def all(self, *args, **keyword_args):
        query_set = super(BenURLManager, self).all(*args, **keyword_args)
        query_set = query_set.filter(active = True)
        return query_set

    def refresh_shortcodes(self, items=None):
        # where the ID is =or bigger than 1
        query_set = BenURL.objects.filter(id__gte = 1)
        # if items is not None and isinstance(items, int):
        #     qs = qs.order_by('id') [:items]
        if items is not None and isinstance(items, int):
        # with -id decrease order by id
            query_set = query_set.order_by('id')[:items]
        new_codes = 0
        # make new shortcode
        for q in query_set:
            q.shortcode = create_shortcode(q)
            print(q.id)
            print(q.url)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made {i}".format(i=new_codes)


class BenURL(models.Model):
    url = models.CharField(max_length=200, )
    # every shortcode should be unique
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank= True)
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
