from rest_framework.views import APIView
from rest_framework.response import Response
from waiter.models import Table


class TableView(APIView):
    """
        View methods for the Table object
    """
    def get(self, request, format=None):
        """
            Returns all the Table objects
        """
        tables = Table.objects.all()
        return Response(tables)
