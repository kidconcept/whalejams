from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import Recording, Species, Population
from .forms import SongFilter

#class RecordingListView(generic.ListView):
	#generic view of recordings for searchin
#	model = Recording
#	paginate_by = 10

#	def get_context_data(self, **kwargs):
#		context = super().get_context_data(**kwargs)

def SongList(request):
# Renders a Form with filters and a list of recordings
	if request.method == 'GET':
		# create a form instance and populate it with data from the request:
		songFilter = SongFilter(request.GET)
		# check whether it's valid:
		if songFilter.is_valid():
			# process the data in songFilter.cleaned_data as required
			# ...
			# redirect to a new URL:
			return reverse('songs')

	# if a GET (or any other method) we'll create a blank songFilter
	else:
		songFilter = SongFilter()

	# get recordings and filter
	filtered_songs = Recording.objects.filter(species__commonName="Humpback Whale")

	# sort recordings
	sorted_songs = filtered_songs.order_by('date')

	# pagination

	return render(
		request, 
		'song_filter.html', 
		{'form': songFilter, 'songs': sorted_songs}
		)
	
class RecordingDetailView(generic.DetailView):
	#generic view of Recording model
	model = Recording

class RecordingCreate(CreateView):
	#generic create recording model form
	model = Recording
	fields = ['file', 'species', 'population', 'lat', 'lon', 'date', 'equipment', 'description', 'commType']	
	initial={'equipment':'H1A Hydrophone'}

def index(request):
	#Da Home page
	#Function to Grab a random recording
	#Doing this the easy way, which is slower than querying total length of the table and random number the length
	def get_random_record(obj):
		return obj.objects.order_by("?").first()

	hero = get_random_record(Recording)

	return render(
		request,
		'index.html',
		#Send the recording parts off to the index
		context={'file':hero.file.url,'commonName':hero.species.commonName,'genusSpecies':hero.species.genusName+" "+hero.species.speciesName,'date':hero.date}
	)