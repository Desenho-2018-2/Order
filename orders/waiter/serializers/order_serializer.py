import serializers
from waiter.models import Order

class OrderSerializer(serializers.Serializer):
    """
    Serializer for Order model
    """
    
    class Meta:
        model = Order
        fields = '__all__'
