from django.contrib import admin

# Register your models here.
from hic.paciente.models import TAlergia, HistoriaClinica

admin.site.register(HistoriaClinica)
