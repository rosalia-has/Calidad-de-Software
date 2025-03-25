# users/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer, RegisterSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Crear el usuario con los datos validados
        user = serializer.save()
        
        # Crear el token JWT para el nuevo usuario
        refresh = RefreshToken.for_user(user)
        
        # Devolver el token junto con el mensaje de éxito
        return Response({
            'message': 'Usuario registrado con éxito.',
            'user': serializer.data,
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }, status=201)

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Obtener los datos del usuario autenticado
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


