from django.urls import path

from . import apis
from .apis import api_view, mixin, generic

app_name = 'snippets'
urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', generic.SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>', generic.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]
