from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
# Create your views here.

from .models import BenURL

def Ben_redirect_view(request, shortcode=None, *args, **kwargs): # function based view
    # in the page the url which belongs to the shortcode (other method)
    try:
        obj = BenURL.objects.get(shortcode = shortcode)
    except:
        # if sg wrong object is the first url
        obj = BenURL.objects.all().first() or "https://www.google.com"

    return HttpResponseRedirect(obj.url)


class BenClassBasedView(View):
    def get(self,  request, shortcode=None, *args, **kwargs):
        # in the page the url which belongs to the shortcode (other method)
        try:
            obj = BenURL.objects.get(shortcode = shortcode)
        except:
            # if sg wrong object is the first url
            obj = BenURL.objects.all().first() or "https://www.google.com"

        return HttpResponseRedirect(obj.url)
