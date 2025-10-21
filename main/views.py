from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import RegistroForm
from .models import Curso, Tema, Subtema, Comentario
import os
from django.shortcuts import render, get_object_or_404
from .models import Encuesta



# PÁGINA PRINCIPAL (HOME)

@login_required
def home(request):
    cursos = Curso.objects.all()
    return render(request, 'home.html', {'cursos': cursos})



# REGISTRO Y LOGIN

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login')



#  CURSOS Y CONTENIDO DINÁMICO

@login_required
def temas(request, curso_nombre):
    curso = get_object_or_404(Curso, nombre=curso_nombre)
    temas = curso.temas.all()
    return render(request, 'temas.html', {
        "curso": curso,
        "temas": temas
    })


@login_required
def subtemas(request, curso_nombre, tema_nombre):
    tema = get_object_or_404(Tema, nombre=tema_nombre, curso__nombre=curso_nombre)
    subtemas = tema.subtemas.all()
    return render(request, 'subtemas.html', {
        "curso": curso_nombre,
        "tema": tema,
        "subtemas": subtemas
    })


@login_required
def detalle(request, curso_nombre, tema_nombre, subtema_nombre):
    subtema = get_object_or_404(
        Subtema,
        nombre=subtema_nombre,
        tema__nombre=tema_nombre,
        tema__curso__nombre=curso_nombre
    )
    
    video_url = subtema.video_url
    if "watch?v=" in video_url:
        video_url = video_url.replace("watch?v=", "embed/")
    elif "youtu.be/" in video_url:
        video_url = video_url.replace("youtu.be/", "www.youtube.com/embed/")

    return render(request, 'detalle.html', {
        "curso": curso_nombre,
        "tema": tema_nombre,
        "subtema": subtema.nombre,
        "video_url": video_url,
        "explicacion": subtema.explicacion
    })



# CUENTA DE USUARIO

@login_required
def cuenta(request):
    user = request.user

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        foto = request.FILES.get('foto_perfil')

        if username:
            user.username = username
        if password:
            user.set_password(password)
        if foto:
            user.foto_perfil = foto

        user.save()

        if password:
            update_session_auth_hash(request, user)

        messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
        return redirect('cuenta')

    return render(request, 'cuenta.html', {'user': user})



# COMENTARIOS

@login_required
def comentarios(request):
    if request.method == "POST":
        texto = request.POST.get("texto", "").strip()
        if texto:
            Comentario.objects.create(usuario=request.user, contenido=texto)
            messages.success(request, "Tu comentario se ha publicado correctamente.")
            return redirect("comentarios")
        else:
            messages.error(request, "No puedes publicar un comentario vacío.")

    comentarios = Comentario.objects.select_related("usuario").order_by("-fecha")
    return render(request, "comentarios.html", {"comentarios": comentarios})


@login_required
def encuesta(request, curso, tema_nombre):
    # Buscar el tema dentro del curso
    tema = get_object_or_404(Tema, nombre=tema_nombre, curso__nombre=curso)

    # Obtener la encuesta asociada al tema
    encuesta = get_object_or_404(Encuesta, tema=tema)

    # Obtener preguntas relacionadas (related_name='preguntas' en el modelo)
    preguntas = encuesta.preguntas.all()

    return render(request, "encuesta.html", {
        "tema": tema,
        "encuesta": encuesta,
        "preguntas": preguntas,
        "curso": curso,
    })