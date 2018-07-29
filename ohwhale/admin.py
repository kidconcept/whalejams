from django.contrib import admin

# Register your models here.
from .models import Recording, Species, Population

admin.site.register(Recording)
admin.site.register(Species)
admin.site.register(Population)
