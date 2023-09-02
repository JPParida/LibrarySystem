from rest_framework import viewsets
from .models import Book, BorrowedBook, RenewalHistory
from .serializers import BookSerializer, BorrowedBookSerializer, RenewalHistorySerializer

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowedBookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer

class RenewalHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RenewalHistory.objects.all()
    serializer_class = RenewalHistorySerializer
