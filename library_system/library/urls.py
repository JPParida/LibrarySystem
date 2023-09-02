from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BorrowedBookViewSet, RenewalHistoryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'borrowed-books', BorrowedBookViewSet)
router.register(r'renewal-history', RenewalHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Add any additional URLs as needed.
]
