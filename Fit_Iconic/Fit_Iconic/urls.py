# Fit_Iconic/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterView, ProfileView
from django.views.generic import TemplateView  # Para renderizar plantillas HTML

urlpatterns = [
    # -------------------
    # Rutas de la API
    # -------------------

    # Ruta para registrar un nuevo usuario (creación)
    path('api/register/', RegisterView.as_view(), name='register'),

    # Ruta para obtener el token JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Ruta para refrescar el token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Ruta para obtener el perfil del usuario autenticado
    path('api/profile/', ProfileView.as_view(), name='profile'),

    # -------------------
    # Rutas de la Interfaz de Usuario
    # -------------------

    # Ruta para la página de inicio (root) que renderiza un HTML
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Redirige a la plantilla index.html

]
