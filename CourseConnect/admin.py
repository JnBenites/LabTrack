from django.contrib import admin
from .models import Institucion, PeriodoAcademico, Cargo, Administrativo, Titulo, Asignatura, Curso, Alumno, Matricula
# Register your models here.
admin.site.register(Institucion)
admin.site.register(PeriodoAcademico)
admin.site.register(Cargo)
admin.site.register(Administrativo)
admin.site.register(Titulo)
admin.site.register(Asignatura)
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Matricula)
