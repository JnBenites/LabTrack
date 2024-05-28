from django.db import models

# Create your models here.

class Institucion(models.Model):
    IdInstitucion = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200)

class PeriodoAcademico(models.Model):
    IdPeriodoAcademico =  models.AutoField(primary_key=True)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()

class Cargo(models.Model):
    IdCargo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200)

class Administrativo(models.Model):
    IdAdministrativo = models.AutoField(primary_key=True)
    Nombres =  models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    Cedula = models.CharField(max_length=10)
    Cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)

class Titulo(models.Model):
    IdTitulo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Nivel = models.CharField(max_length=50)
    Registrosenescyt = models.CharField(max_length=100)
    
class Asignatura(models.Model):
    IdAsignatura =  models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    IdAdministrativo = models.ForeignKey(Administrativo, on_delete=models.PROTECT, null=True, blank=True)

class Curso(models.Model):
    IdCurso =  models.AutoField(primary_key=True)
    IdPeriodoAcademico = models.ForeignKey(PeriodoAcademico, on_delete=models.PROTECT)
    IdAsignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)

class Alumno(models.Model):
    IdAlumno = models.AutoField(primary_key=True)
    Nombres =  models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    Cedula = models.CharField(max_length=10)

class Matricula(models.Model):
    IdMatricula = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo_academico = models.ForeignKey(PeriodoAcademico, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)
