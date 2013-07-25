from django.http import HttpResponse
from django.template import Context, loader
from imagetest.models import Test
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
	entries = Test.objects.all()
	return render_to_response('imagetest/upload.html', RequestContext(request, {'entries': entries}))

