import logging

from rest_framework.views import APIView
from rest_framework.response import Response

class OrderView(APIView):
    """
    This class manager a Order
    """

    def post(self, request, format=None):
        """
        Get a Http POST method from Tasker
        """
        
        logging.warn(request.data)

        return Response('complete!')
