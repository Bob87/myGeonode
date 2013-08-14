from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import Context, loader
from imagetest.models import Test
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from imagetest.forms import *
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from geonode.security.enumerations import AUTHENTICATED_USERS, ANONYMOUS_USERS
from geonode.security.views import _perms_info
import os.path

@login_required
def home(request):
        if request.method == 'POST':
		out = {}
		try:
			form = TestForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				land = cd['land']
				hydro = cd['hydro']
				timehorz = cd['timehorz']
				hydromodel = cd['hydromodel']
				climateforcing = cd['climateforcing']
				climatedatapro = cd['climatedatapro']
				spatialscales = cd['spatialscales']
				if (timehorz != 'BOTH') and (climateforcing != 'ALL'):
					output = land+'_'+hydro+'_'+timehorz+'_'+hydromodel+'_'+climateforcing+'_'+climatedatapro+'_'+spatialscales+'.csv'
					img = Test.objects.get(csv=output)
					return render_to_response('imagetest/add.html',{'form': form, 'land':land,'hydro':hydro, 'output': output, 'img':img},context_instance=RequestContext(request))
				elif (timehorz == 'BOTH') and (climateforcing != 'ALL'):
					output = land+'_'+hydro+'_'+'REF'+'_'+hydromodel+'_'+climateforcing+'_'+climatedatapro+'_'+spatialscales+'.csv'
					output2 = land+'_'+hydro+'_'+'FUT'+'_'+hydromodel+'_'+climateforcing+'_'+climatedatapro+'_'+spatialscales+'.csv'
					img2 = Test.objects.get(csv=output)
					img3 = Test.objects.get(csv=output2)
					return render_to_response('imagetest/add.html',{'form': form, 'land':land,'hydro':hydro, 'output': output,'output2': output2, 'img2':img2,'img3':img3},context_instance=RequestContext(request))
				else:
					output = land+'_'+hydro+'_'+timehorz+'_'+hydromodel+'_'+'ERC'+'_'+climatedatapro+'_'+spatialscales+'.csv'
					output3 = land+'_'+hydro+'_'+timehorz+'_'+hydromodel+'_'+'ERM'+'_'+climatedatapro+'_'+spatialscales+'.csv'
					output4 = land+'_'+hydro+'_'+timehorz+'_'+hydromodel+'_'+'ERE'+'_'+climatedatapro+'_'+spatialscales+'.csv'
					output5 = land+'_'+hydro+'_'+timehorz+'_'+hydromodel+'_'+'HRC'+'_'+climatedatapro+'_'+spatialscales+'.csv'
					output6 = land+'_'+hydro+'_'+timehorz+'_'+hydromodel+'_'+'ALL'+'_'+climatedatapro+'_'+spatialscales+'.csv'
					img = Test.objects.get(csv=output6)
					return render_to_response('imagetest/add.html',{'form': form, 'land':land,'hydro':hydro, 'output': output,'output3': output3, 'output4': output4, 'output5': output5, 'output6': output6, 'img':img},context_instance=RequestContext(request))
		except Exception, e:
			out['errors'] = str(e)
			return render_to_response('imagetest/add.html',{'out': out},context_instance=RequestContext(request))
	else:
			form=TestForm()
        return render_to_response('imagetest/upload.html',{'form': form}, context_instance=RequestContext(request))

