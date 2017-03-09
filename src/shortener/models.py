from django.db import models
import datetime

# Create your models here.
class BenURL(models.Model):
    url = models.CharField(max_length=200, )
    # every shortcode should be unique
    shortcode = models.CharField(max_length=15, unique=True)
    # when was the model created
    created_datetime = models.DateTimeField(auto_now = True)
    #  when was the model modified last time
    update_timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return set(self.url)
