from django.urls import path

from . import apis
from .apis import api_view, mixin

app_name = 'snippets'
urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', mixin.SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>', mixin.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]
