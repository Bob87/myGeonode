import os
from django import forms
from imagetest.modelOutput import LAND_INDICATOR, HYDROLOGICAL_INDICATOR

class TestForm(forms.Form):
	land = forms.ChoiceField(choices=LAND_INDICATOR, label=u'Land')
	#hydro = forms.ChoiceField(choices=HYDROLOGICAL_INDICATOR, label=u'hydrological indicator')
