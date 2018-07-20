from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Recording, Species, Population, Document

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

class DocumentCreateView(CreateView):
	model = Document
	fields = ['upload', ]
	success_url = reverse_lazy('home')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		documents = Document.objects.all()
		context['documents'] = documents
		return context