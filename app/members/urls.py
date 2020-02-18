from django.urls import path

from snippets import apis

urlpatterns = [
    path('auth-token', apis.AuthTokenAPIView.as_view),
]
