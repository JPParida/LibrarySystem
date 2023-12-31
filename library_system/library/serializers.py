from rest_framework import serializers
from .models import Book, BorrowedBook, RenewalHistory

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = '__all__'

class RenewalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RenewalHistory
        fields = '__all__'
