from django.shortcuts import render

# Create your views here.
from ..models.author import Author
from ..models.book import Book
from ..models.book_instance import BookInstance

def index(request):
    
    book = Book.objects.all()
    author = Author.objects.all()
    book_instance = BookInstance.objects.all()
    
    return render(
        request,
        'catalog/index.html',
        context=
        {
            "book":book,
            "author":author,
            "book_instance":book_instance
        }
    )  