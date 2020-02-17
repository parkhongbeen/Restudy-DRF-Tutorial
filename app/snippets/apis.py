from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetListCreateAPIView(APIView):
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Snippet, pk=pk)

    def get(self, request, pk):
        snippet = self.object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer)

    def patch(self, request, pk):
        snippet = self.object(pk)
        serializer = SnippetSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        snippet = self.object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
