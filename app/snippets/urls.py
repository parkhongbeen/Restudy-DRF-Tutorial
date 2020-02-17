from django.urls import path

from . import apis
from .apis import api_view

app_name = 'snippets'
urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', api_view.SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>', api_view.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]
