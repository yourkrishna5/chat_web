from rest_framework import serializers
from .models import Chat

class Seri(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields="__all__"