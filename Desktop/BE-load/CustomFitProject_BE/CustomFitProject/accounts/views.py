from rest_framework import viewsets
from .serializers import UserSerializer, UserUpdateSerializer
from django.contrib.auth.models import User
from .permissions import IsOwner

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsOwner]
    serializer_class = UserSerializer  # Serializer 클래스 지정

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return self.serializer_class
