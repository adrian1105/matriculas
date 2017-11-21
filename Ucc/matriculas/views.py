from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django. contrib.auth.mixins import LoginRequiredMixin

from matriculas.models import Alumno, Curso, Matricula


class AlumnoList(LoginRequiredMixin, ListView):
    model = Alumno
    fields = ['nombres']
    context_object_name = 'matriculas'
    template_name = 'matriculas/alumno_lista.html'


class AlumnoUpdate(LoginRequiredMixin, UpdateView):
    model = Alumno
    fields = ['nombres', 'primer_apellido', 'segundo_apellido']
    template_name = 'matriculas/actualizar_alumnos.html'
    success_url = reverse_lazy('alumno')


class AlumnoDelete(LoginRequiredMixin, DeleteView):
    model = Alumno
    template_name = 'matriculas/eliminar-alumnos.html'
    success_url = reverse_lazy('alumno')


class AlumnoCreate(LoginRequiredMixin, CreateView):
    model = Alumno
    fields = [
        'nombres',
        'primer_apellido',
        'segundo_apellido',
        'cedula',
        'sexo',
        'ciudad_nacimiento'
    ]
    template_name = 'matriculas/crear-alumnos.html'
    success_url = reverse_lazy('alumno')


class AlumnoDetail(LoginRequiredMixin, DetailView):
    model = Alumno
    template_name = 'matriculas/alumnos_datails.html'


class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    context_object_name = 'matriculas'


class CursoCreate(LoginRequiredMixin, CreateView):
    model = Curso
    fields = [
        'nombre',
        'creditos',
        'estado'
    ]
    template_name = 'matriculas/crear-cursos.html'
    success_url = reverse_lazy('crear-cursos')


class MatriculaCreate(LoginRequiredMixin, CreateView):
    model = Matricula
    fields = [
        'alumno',
        'curso'
    ]
    template_name = 'matriculas/realizar-matricula.html'
    success_url = reverse_lazy('realizar-matricula')


class IndexPageView(LoginRequiredMixin, TemplateView):
    template_name = "matriculas/index.html"
