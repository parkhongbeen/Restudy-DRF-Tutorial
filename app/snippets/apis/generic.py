from rest_framework import generics, permissions

from ..models import Snippet
from ..serializers import SnippetSerializer, SnippetCreateSerializer


class SnippetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SnippetSerializer

        elif self.request.method == 'POST':
            return SnippetCreateSerializer

        def perform_create(self, serializer):
            serializer.save(author=self.request.user)
