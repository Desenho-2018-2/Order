from rest_framework import serializers
from waiter.models import OrderPad


class OrderPadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPad
        fields = '__all__'
