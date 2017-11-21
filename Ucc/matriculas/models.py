from django.db import models


class Alumno(models.Model):
    nombres = models.CharField(max_length=40)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=10)
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    ciudad_nacimiento = models.CharField(max_length=40)

    def NombreCompleto(self):
        cadena = "{0} {1} {2}"
        return cadena.format(
            self.nombres,
            self.primer_apellido,
            self.segundo_apellido
            )

    def __str__(self):
        return self.NombreCompleto()


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    creditos = models.PositiveSmallIntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.nombre, self.creditos)


class Matricula(models.Model):
    alumno = models.ForeignKey(
        Alumno,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    curso = models.ForeignKey(
        Curso,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    fecha_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Alumno, self.Curso)
