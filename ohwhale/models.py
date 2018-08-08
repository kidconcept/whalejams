from django.db import models
from django.urls import reverse
import uuid
from datetime import timedelta
from datetime import date
from django.contrib import admin

# Create your models here.
class Recording(models.Model):
	"""
	Recordings are user uploaded, meta tagged, whale recordings.
	"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	file = models.FileField(help_text="The recording you made.")
	species = models.ForeignKey('Species', on_delete=models.SET_NULL, null=True, help_text="Choose the species of cetacean in this recording")
	population = models.ForeignKey('Population', on_delete=models.SET_NULL, null=True, blank=True, help_text="Choose the population")
	lat = models.DecimalField(max_digits=10, decimal_places=7)
	lon = models.DecimalField(max_digits=10, decimal_places=7)
	date = models.DateField(help_text="The date your recording was made", null=True)
	uploaded_on = models.DateField(auto_now_add=True)
	equipment = models.CharField(max_length=64, blank=True)
	description = models.TextField(max_length=560, blank=True)
	length = models.DurationField(null=True, blank=True)

	COMM_TYPE = (
		('a', 'song'),
		('b', 'signal')
	)
	commType = models.CharField(max_length=6, choices=COMM_TYPE, blank=True, default='a', help_text="Is this song or other communication?")

	def __str__(self):

		if self.population is None:
			pop = 'Population Unknown'
		else:
			pop = self.population.population

		return f'{self.species.commonName}, {pop}, {self.uploaded_on}, {str(self.id)}'

	def get_absolute_url(self):
		return reverse('song-detail', args=[str(self.id)])


class Species(models.Model):
	"""
	Species of cetacea in the recording, eg Humpback Whale
	"""
	speciesName = models.CharField(max_length=32)
	genusName = models.CharField(max_length=32)
	commonName = models.CharField(max_length=64)

	def __str__(self):
		return self.commonName

class Population(models.Model):
	"""
	population of cetacea, eg North Atlantic Population
	"""
	population = models.CharField(max_length=32)

	def __str__(self):
		return self.population

#class Recording(admin.ModelAdmin):
#	change_form_template = 'progressbarupload/change_form.html'
#	add_form_template = 'progressbarupload/change_form.html'