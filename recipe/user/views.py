from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserViews(generics.CreateAPIView):
    """Create a new user in the system via api"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new token view for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES