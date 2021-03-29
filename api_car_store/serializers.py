from rest_framework import serializers

from .models import Dealer, Car


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ('name', 'city')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('dealer_id', 'name', 'price', 'color')
