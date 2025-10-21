from django.urls import path
from django.shortcuts import redirect
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('home/', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('curso/<str:curso_nombre>/', views.temas, name='temas'),
    path('curso/<str:curso_nombre>/<str:tema_nombre>/', views.subtemas, name='subtemas'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('curso/<str:curso>/<str:tema_nombre>/encuesta/', views.encuesta, name='encuesta'),
    path('curso/<str:curso_nombre>/<str:tema_nombre>/<str:subtema_nombre>/', views.detalle, name='detalle'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)