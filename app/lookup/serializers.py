"""
Serializers for the user API View.
"""
from core.models import Services

from rest_framework import serializers


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'name']
