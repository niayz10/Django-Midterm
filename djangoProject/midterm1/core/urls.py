
from django.urls import path, include

from core.views import BookViewSet, JournalViewSet

urlpatterns = [
    path('books', BookViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:id>', BookViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
    path('journals', JournalViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('journals/<int:id>', JournalViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
]