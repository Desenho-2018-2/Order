from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from waiter.models import OrderPad
from waiter.serializers import OrderPadSerializer


class OrderPadView(APIView):
    """
        View methods for the OrderPad object
    """

    authentication_classes = []

    def get(self, request, format=None):
        """
            Returns all OrderPad objects
        """
        orderpads = OrderPad.objects.all()
        serialized_orderpads = OrderPadSerializer(orderpads, many=True)
        return Response(serialized_orderpads.data)

    def post(self, request, format=None):
        """
            Inserts an orderpad in the database
        """
        orderpad_serializer = OrderPadSerializer(data=request.data)

        if orderpad_serializer.is_valid():
            orderpad_serializer.save()

            return Response(orderpad_serializer.data)


@api_view(['GET'])
def get_orderpad(request, pk, format=None):
    """
        Returns a specific OrderPad by its id
    """

    try:
        orderpad = OrderPad.objects.get(pk=pk)

        serialized_orderpad = OrderPadSerializer(orderpad)

        return Response(serialized_orderpad.data)
    except:
        raise Http404
