from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Recording, Species, Population
from .forms import NewRecordForm


# Create your views here.
def index(request):

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

class RecordingDetailView(generic.DetailView):
	model = Recording

# These views are all attempts to render the upload form

def upload_recording(request):
	if request.method == 'POST':
		form = NewRecordForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/new-record/')
	else:
		form = NewRecordForm()
	return render(request, 'upload_recording.html', {'form': form})

class RecordingCreate(CreateView):
	model = Recording
	fields = ['file', 'species', 'population', 'lat', 'lon', 'date', 'equipment', 'description', 'commType']	
	initial={'equipment':'H1A Hydrophone'}

class RecordingUpdate(UpdateView):
	model = Recording
	fields = ['file', 'species', 'population', 'lat', 'lon', 'date', 'equipment', 'description', 'commType']

class RecordingDelete(DeleteView):
	model = Recording
	#success_url = reverse_lazy('recordings')