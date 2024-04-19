from rest_framework import serializers
from .models import *

class GameSerializer(serializers.ModelSerializer):
    def validate_price(self, value):
        if not isinstance(value, (int, float)):
            raise serializers.ValidationError('Цена должна быть числом')
        if value < 0.1 or value > 1000:
            raise serializers.ValidationError('Цена должна быть в диапазоне от 0.1 до 1000')
        return value

    class Meta:
        model = Game
        fields = "__all__"
    