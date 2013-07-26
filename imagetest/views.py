from django.http import HttpResponse
from django.template import Context, loader
from imagetest.models import Test
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from imagetest.forms import TestForm
from django.core.context_processors import csrf

def home(request):
	form = TestForm()
	entries = Test.objects.all()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('imagetest/upload.html', args)

#	return render_to_response('imagetest/upload.html', RequestContext(request,{'form':form, 'entries': entries,}), args)
