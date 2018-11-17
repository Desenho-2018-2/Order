from rest_framework.views import APIView
from rest_framework.response import Response
from waiter.models import Table
from waiter.serializers import TableSerializer


class TableView(APIView):
    """
        View methods for the Table object
    """
    def get(self, request, format=None):
        """
            Returns all the Table objects
        """
        tables = Table.objects.all()
        serialized_tables = TableSerializer(tables, many=True)
        return Response(serialized_tables.data)
