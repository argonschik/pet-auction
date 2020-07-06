from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.auction.models import Lot, Bet

User = get_user_model()


class LotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        fields = [
            'id', 'starting_price', 'pet', 'seller', 'status',
        ]

    def update(self, instance, validated_data):
        new_status = validated_data.get('status', instance.status)
        if new_status == instance.Status.CLOSED:
            instance.close()
        return instance


class BetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bet
        fields = [
            'id', 'bid', 'buyer', 'lot',
        ]

