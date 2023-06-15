from django.db import models
from .author import Author
from .genre import Genre
from .language import Language
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.OneToOneField(Author,on_delete= models.CASCADE)
    summary = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre,null = True,on_delete= models.SET_NULL)
    language = models.ForeignKey(Language,null = True,on_delete= models.SET_NULL)
    
    def __str__(self) :
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
