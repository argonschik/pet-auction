from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.pet.models import Pet

User = get_user_model()


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = [
            'id', 'breed', 'nickname', 'owner',
        ]

