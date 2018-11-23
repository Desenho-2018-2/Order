import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders.serializer import OrderSerializer

logging.basicConfig(level=logging.DEBUG)

class NotifyOrder(APIView):
    """
    This class manager a Order
    """

    def post(self, request, format=None):
        """
        Get a Http POST method from Tasker and save the model
        """

        notify_serializer = OrderSerializer(data=request.data)
        status_response = None

        if notify_serializer.is_valid():

            order_model = notify_serializer.save()
            status_response = status.HTTP_200_OK

        else:
            logging.debug("Notify Order BAD REQUEST")


            status_response = status.HTTP_400_BAD_REQUEST
        

        return Response(status=status_response)
