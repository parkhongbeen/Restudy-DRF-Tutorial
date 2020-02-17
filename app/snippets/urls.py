from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis import generic, viewsets

app_name = 'snippets'

router = DefaultRouter()
router.register(r'snippets', viewsets.SnippetViewSet)

# router.urls는 아래 urlpatterns_viewset의 모든 내용이 들어있음
urlpatterns_viewset = [
    path('snippets/', viewsets.SnippetViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('snippets/', viewsets.SnippetViewSet.as_view({
        'get': 'Retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
]

urlpatterns_api_view = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', generic.SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>', generic.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]

urlpatterns = [
    path('api_view/', include(urlpatterns_api_view)),
    path('viewset/', include(urlpatterns_viewset)),
    path('router/', include(router.urls)),

]
