from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Agrega campos personalizados si lo necesitas
    pass
from django.urls import path
from users.views import RegisterView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



