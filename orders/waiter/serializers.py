from rest_framework import serializers
from waiter.models import Table


class TableSerializer(serializers.ModelSerializer):
    """
        Serializer for the Table object
    """
    class Meta:
        model = Table
        fields = '__all__'
