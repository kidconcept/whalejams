from django import forms
from .models import Recording


from s3direct.widgets import S3DirectWidget
class NewRecordForm(forms.ModelForm):
	file = forms.URLField(widget=S3DirectWidget(dest='whalejams'))

	class Meta:
		model = Recording
		fields = ('file', 'lat', 'lon')