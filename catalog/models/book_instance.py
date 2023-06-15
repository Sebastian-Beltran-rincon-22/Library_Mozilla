from django.db import models
from .book import Book

class BookInstance(models.Model):
    unique_id = models.CharField(max_length=50)
    due_back = models.DateField(default=0)
    status = models.CharField(max_length=40)
    book = models.ForeignKey(Book, null = True, on_delete=models.SET_NULL)
    imprint = models.CharField(max_length=50)
    borrower = models.CharField(max_length=30)

    def __str__(self):
        return self.unique_id
    