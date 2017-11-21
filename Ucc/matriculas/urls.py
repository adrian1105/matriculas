from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from matriculas.views import (
    AlumnoList,
    AlumnoCreate,
    AlumnoDetail,
    CursoList,
    IndexPageView,
    CursoCreate,
    MatriculaCreate,
    AlumnoUpdate,
    AlumnoDelete
)

urlpatterns = [
    url(
        r'alumno/$',
        AlumnoList.as_view(),
        name='alumno'
        ),
    url(
        r'^(?P<pk>\d+)/$',
        AlumnoUpdate.as_view(),
        name='actualizar-alumno'
        ),
    url(
        r'^eliminar/(?P<pk>\d+)/$',
        AlumnoDelete.as_view(),
        name='eliminar-alumno'
        ),
    url(
        r'^login/$',
        LoginView.as_view(
            template_name='matriculas/login.html'
            ),
        name='login'
        ),
    url(
        r'^logout/$',
        LogoutView.as_view(next_page=reverse_lazy('login')),
        name='logout'
    ),
    url(
        r'index/$',
        IndexPageView.as_view(),
        name='index'),
    url(
        r'^crear-alumnos/$',
        AlumnoCreate.as_view(),
        name='crear-alumnos'
    ),
    url(
        r'^detalles/(?P<pk>\d+)/$',
        AlumnoDetail.as_view(),
        name='detail'
    ),
    url(
        r'curso/$',
        CursoList.as_view(),
        name=''
        ),
    url(
        r'^crear-cursos/$',
        CursoCreate.as_view(),
        name='crear-cursos'
        ),
    url(
        r'^crear-matricula/$',
        MatriculaCreate.as_view(),
        name='realizar-matricula'
        )
]
