from django.contrib import admin

from matriculas.models import Alumno, Curso, Matricula


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cedula',
        'nombres',
        'primer_apellido',
        'segundo_apellido'
    ]
    search_fields = [
        'cedula',
        'nombres',
        'primer_apellido'
    ]


admin.site.register(Curso)
admin.site.register(Matricula)
