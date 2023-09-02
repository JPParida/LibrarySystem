from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    total_copies = models.PositiveIntegerField(default=0)
    
class BorrowedBook(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    due_date = models.DateField()
    renewed = models.BooleanField(default=False)
    
class RenewalHistory(models.Model):
    borrowed_book = models.ForeignKey(BorrowedBook, on_delete=models.CASCADE)
    renewal_date = models.DateField(auto_now_add=True)
    
# Add any additional fields or models as needed.
