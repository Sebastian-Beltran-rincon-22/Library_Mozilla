from django.shortcuts import render

# Create your views here.
from ..models.author import Author
from ..models.book import Book

def index(request):
    
    book = Book.objects.all()
    author = Author.objects.all()
    
    return render(
        request,
        'catalog/index.html',
        context=
        {
            "book":book,
            "author":author
        }
    )  