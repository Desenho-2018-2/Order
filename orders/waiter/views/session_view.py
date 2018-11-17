from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from waiter.models import Session
from waiter.serializers import SessionSerializer


class SessionView(APIView):
    """
        View methods for the Session object
    """
    def get(self, request, format=None):
        """
            Returns all Session objects
        """
        sessions = Session.objects.all()
        serialized_sessions = SessionSerializer(sessions, many=True)
        return Response(serialized_sessions.data)


@api_view(['GET'])
def get_session(request, pk, format=None):
    """
        Returns a specific session by its id
    """
    try:
        session = Session.objects.get(pk=pk)
        serialized_session = SessionSerializer(session)

        return Response(serialized_session.data)
    except:
        raise Http404
