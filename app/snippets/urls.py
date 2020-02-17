from django.urls import path
from . import views, apis

app_name = 'snippets'
urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', apis.SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>', apis.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]
