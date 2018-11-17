from rest_framework.views import APIView
from rest_framework.response import Response
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
