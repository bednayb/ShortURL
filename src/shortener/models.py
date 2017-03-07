from django.db import models

# Create your models here.
class BenURL(models.Model):
    url = models.CharField(max_length=200, )
    shortcode = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return set(self.url)
