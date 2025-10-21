from django.contrib import admin
from .models import Comentario, Curso, Tema, Subtema, Encuesta, Pregunta

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'contenido', 'fecha')
    search_fields = ('usuario__username', 'contenido')
    list_filter = ('fecha',)
    # Aquí se podrán eliminar comentarios inapropiados


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curso')
    list_filter = ('curso',)
    search_fields = ('nombre',)


@admin.register(Subtema)
class SubtemaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tema', 'video_url')
    list_filter = ('tema__curso',)
    search_fields = ('nombre',)
    # Aquí se podrá poner la info de los cursos


class PreguntaInline(admin.TabularInline):
    model = Pregunta
    extra = 1


class PreguntaInline(admin.TabularInline):
    model = Pregunta
    extra = 1


@admin.register(Encuesta)
class EncuestaAdmin(admin.ModelAdmin):
    inlines = [PreguntaInline]
    list_display = ("titulo", "tema")
    search_fields = ("titulo", "tema__nombre")


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("texto", "encuesta")
    search_fields = ("texto",)