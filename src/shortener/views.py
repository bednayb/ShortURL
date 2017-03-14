from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

def Ben_redirect_view(request, shortcode=None, *args, **kwargs): # function based view
    return  HttpResponse("hey {sc}".format(sc=shortcode))

class BenClassBasedView(View):
    def get(self, request, *args, **kwargs):
        return  HttpResponse("hey {sc}".format(sc=shortcode))
