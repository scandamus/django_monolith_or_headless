from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DataOmikuji


class OmikujiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataOmikuji
        fields = ['id', 'nick_name', 'result', 'created_at']
