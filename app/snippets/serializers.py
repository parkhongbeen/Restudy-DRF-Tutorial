from rest_framework import serializers

from .models import Snippet


class SnippetSerializer(serializers.Serializer):
    class Meta:
        model = Snippet

    fields = {
        'pk',
        'author',
        'title',
        'code',
        'linenos',
        'language',
        'style',
        'created',
    }


class SnippetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        field = (
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'created',
        )

    def to_representation(self, instance):
        return SnippetSerializer(instance).data
