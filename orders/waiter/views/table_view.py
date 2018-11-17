from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from waiter.models import Table
from waiter.serializers import TableSerializer


class TableView(APIView):
    """
        View methods for the Table object
    """

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """
            Returns all Table objects
        """
        tables = Table.objects.all()
        serialized_tables = TableSerializer(tables, many=True)
        return Response(serialized_tables.data)

    @csrf_exempt
    def post(self, request, format=None):
        table_serializer = TableSerializer(data=request.data)

        if table_serializer.is_valid():
            table_serializer.save()
            return Response(table_serializer.data)


@api_view(['GET'])
def get_table(request, pk, format=None):
    """
        Returns a specific table by its id
    """
    try:
        table = Table.objects.get(pk=pk)

        serialized_table = TableSerializer(table)

        return Response(serialized_table.data)
    except:
        raise Http404
