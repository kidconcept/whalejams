from django import forms

class NewRecordForm(forms.Form):
	species_name = forms.CharField(label="species_name")