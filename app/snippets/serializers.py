from rest_framework import serializers

from .models import Snippet


class SnippetSerializer(serializers.Serializer):
    class Meta:
        model = Snippet

    fields = {
        'pk',
        'title',
        'code',
        'linenos',
        'language',
        'style',
        'created',
    }
