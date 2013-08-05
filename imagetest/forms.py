from django import forms
from imagetest.modelOutput import LAND_INDICATOR, HYDROLOGICAL_INDICATOR, TIME_HORIZON, HYDROLOGICAL_MODEL, CLIMATE_FORCING,CLIMATE_DATA_PROCESSING, SPATIAL_SCALES

class TestForm(forms.Form):
	land = forms.ChoiceField(choices=LAND_INDICATOR, label=u'Land',required=True)
	hydro = forms.ChoiceField(choices=HYDROLOGICAL_INDICATOR, label=u'hydrological indicator')
	timehorz = forms.ChoiceField(choices=TIME_HORIZON, label=u'Time Horizon')
	hydromodel = forms.ChoiceField(choices=HYDROLOGICAL_MODEL, label=u'Hydrological model')
	climateforcing = forms.ChoiceField(choices=CLIMATE_FORCING, label=u'Climate forcing')
	climatedatapro = forms.ChoiceField(choices=CLIMATE_DATA_PROCESSING, label=u'Climate data processing')
	spatialscales = forms.ChoiceField(choices=SPATIAL_SCALES, label=u'Spatial scales')
	#output = forms.CharField()

	def __init__(self, *args, **kwargs):
		super(TestForm, self).__init__(*args, **kwargs)
		self.fields['land'].initial = 'Rio Mannu'

	
