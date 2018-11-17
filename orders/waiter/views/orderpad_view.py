from rest_framework.views import APIView
from rest_framework.response import Response
from waiter.models import OrderPad
from waiter.serializers import OrderPadSerializer


class OrderPadView(APIView):
    """
        View methods for the OrderPad object
    """
    def get(self, request, format=None):
        """
            Return all OrderPad objects
        """
        orderpads = OrderPad.objects.all()
        serialized_orderpads = OrderPadSerializer(orderpads, many=True)
        return Response(serialized_orderpads.data)
