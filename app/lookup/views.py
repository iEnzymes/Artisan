"""
Views for the lookup API.
"""
from rest_framework import generics, authentication, permissions
from core.models import UserType

from lookup.serializers import (
    ServicesSerializer
)


class ServicesView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserType.objects.all()
    serializer_class = ServicesSerializer
