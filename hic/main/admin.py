from django.contrib import admin
from hic.main.models import *

# Register your models here.
admin.site.site_header = "Sistema de gestión de médico"
admin.site.site_title = "Sistema de gestión de médico"
admin.site.index_title = "Bienvenido al sistema"

class RegistroIncidenciasAdmin(admin.ModelAdmin):
    list_display = ['accion', 'fecha', 'usuario', 'comentario']
    search_fields = ['accion', 'fecha', 'usuario', 'comentario']
    list_filter = ['accion', 'fecha', 'usuario', 'comentario']

admin.site.register(RegistroIncidencias, RegistroIncidenciasAdmin)
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(InicioFolio)
admin.site.register(Especialidad)
# admin.site.register(EspecialidadMedico)
# admin.site.register(NEstado)
# admin.site.register(Institucion)
# admin.site.register(NCodigoPostal)
# admin.site.register(NMunicipio)
