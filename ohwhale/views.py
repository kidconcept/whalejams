from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Recording, Species, Population, RecordingFilter
from .forms import NewRecordForm

from django.views.generic import FormView

# CLEAN THESE IMPORTS YA SLOBP

#Da details View
class RecordingDetailView(generic.DetailView):
	model = Recording

#Da Upload View
def upload(request):

	if request.method == 'POST':
		nRF = NewRecordForm(request.POST)
		if nRF.is_valid():
			new_record = nRF.save()
			return redirect('song-detail',pk=new_record.id)

	else:
		nRF = NewRecordForm()

	return render(
		request,
		'newRecordForm.html',
		context={'newRecordForm':nRF}
	)

#Da Home page
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

#Da Search Page
def song_list(request):
	f = RecordingFilter(request.GET, queryset=Recording.objects.all())

	paginator = Paginator(f.qs, 5)
	page = request.GET.get('page')
	results = paginator.get_page(page)

	return render(
		request, 
		'recording_filter.html', 
		context={'results':results,'filter':f}
	)

