from django import forms

class SongFilter(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)