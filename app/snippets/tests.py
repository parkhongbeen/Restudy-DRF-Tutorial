import random

from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from members.models import User
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetTest(APITestCase):
    def test_snippet_list(self):
        url = '/api-view/snippets/'
        response = self.client.et(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        baker.make(Snippet, __quantity=5)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        for snippet_data in response.data:
            self.assertIn('author', snippet_data)
            self.assertIn('title', snippet_data)
            self.assertIn('code', snippet_data)
            self.assertIn('linenos', snippet_data)
            self.assertIn('language', snippet_data)
            self.assertIn('style', snippet_data)

            self.assertEqual('1', snippet_data['code'])

            pk = snippet_data['pk']
            snippet = Snippet.objects.get(pk=pk)
            self.assertEqual(
                SnippetSerializer(snippet).data,
                snippet_data
            )

    def test_snippet_create(self):
        url = '/api-view/snippets/'
        user = baker.make(User)
        data = {
            'author': user.pk,
            'code': 'def.abc():',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pk = response.data['pk']
        snippet = Snippet.objects.get(pk=pk)
        self.assertEqual(
            response.data,
            SnippetSerializer(snippet).data,
        )
        self.assertEqual(Snippet.objects.count(), 1)

    def test_snippet_delete(self):
        snippets = baker.make(Snippet, _quantity=5)

        snippet = random.choice(snippets)
        url = f'/api-view/snippets/{snippet.pk}/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Snippet.objects.count(), 4)
        self.assertFalse(Snippet.objects.filter(pk=snippet.pk).exists())
