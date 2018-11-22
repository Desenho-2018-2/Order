from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from waiter.models import Session
from waiter.serializers import SessionSerializer


class SessionView(APIView):
    """
        View methods for the Session object
    """

    authentication_classes = []

    def get(self, request, format=None):
        """
            Returns all Session objects
        """
        sessions = Session.objects.all()
        serialized_sessions = SessionSerializer(sessions, many=True)
        return Response(serialized_sessions.data)

    def post(self, request, format=None):
        """
            Inserts a session in the database
        """
        session_serializer = SessionSerializer(data=request.data)

        if session_serializer.is_valid():
            session_serializer.save()
            return Response(session_serializer.data)


class SessionDetailView(APIView):
    """
        View methods for a Session object
    """
    authentication_classes = []

    def get_object(self, pk):
        try:
            return Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
            Returns a specific session by its id
        """
        session = self.get_object(pk)
        serialized_session = SessionSerializer(session)

        return Response(serialized_session.data)

    def put(self, request, pk, format=None):
        """
            Updates a session by its id
        """
        session = self.get_object(pk)
        session_serializer = SessionSerializer(session, data=request.data)

        if session_serializer.is_valid():
            session_serializer.save()
            return Response(session_serializer.data)

        return Response(session_serializer.errors)
