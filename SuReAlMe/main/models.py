from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings    

class User(AbstractUser):
    ROLE_CHOICES = (
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
    )
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default='estudiante')
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return self.username


    @property
    def es_profesor(self):
        return self.rol == 'profesor'

    @property
    def es_alumno(self):
        return self.rol == 'estudiante'

class Comentario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.contenido[:30]}"


class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Tema(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='temas')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.curso.nombre} - {self.nombre}"


class Subtema(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='subtemas')
    nombre = models.CharField(max_length=100)
    video_url = models.URLField(blank=True, null=True)
    explicacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tema.nombre} - {self.nombre}"



class Encuesta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class Encuesta(models.Model):
    tema = models.OneToOneField(Tema, on_delete=models.CASCADE, related_name="encuesta")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"Encuesta de {self.tema.nombre}"
    

class Pregunta(models.Model):
    encuesta = models.ForeignKey(
        Encuesta,
        on_delete=models.CASCADE,
        related_name='preguntas'
    )
    texto = models.CharField(max_length=300)
    opcion1 = models.CharField(max_length=150)
    opcion2 = models.CharField(max_length=150)
    opcion3 = models.CharField(max_length=150)
    opcion4 = models.CharField(max_length=150)
    respuesta_correcta = models.CharField(max_length=150)

    def __str__(self):
        return self.texto
