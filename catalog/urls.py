from django.urls import path

from .views import views
from .views import author
from .views import book_instance
from .views import book
from .views import language
from .views import genre

urlpatterns = [
    path('',views.index,name="index") 
]

urlpatterns += [
    path("author",author.AuthorListView.as_view(),name="author"),
    path("author/<int:pk>",author.AuthorDetailView.as_view(),name='author_detail'),
    path("author/create",author.AuthorCreateView.as_view(),name='create_author')
]

urlpatterns += [
    path("book_instance",book_instance.BookInstanceListView.as_view(),name='book_instance'),
    path("book_instance/<int:pk>",book_instance.BookInstanceDetailtView.as_view(),name='book_instance_detail'),
    path("book_instance/create",book_instance.BookInstanceCreateView.as_view(),name= 'create-book_instance')
]

urlpatterns += [
    path("book",book.BookListView.as_view(),name='book'),
    path("book/<int:pk>",book.BookDetailtView.as_view(),name='book_detail'),
    path("book/create",book.BookCreateView.as_view(),name= 'create_book')
]

urlpatterns += [
    path("language",language.LanguageListView.as_view(),name='language'),
    path("language/<int:pk>",language.LanguageDetailtView.as_view(),name='language_detail'),
    path("language/create",language.LanguageCreateView.as_view(),name= 'create_language')
]
urlpatterns += [
    path("genre",genre.GenreListView.as_view(),name='genre'),
    path("genre/<int:pk>",genre.GenreDetailtView.as_view(),name='genre_detail'),
    path("genre/create",genre.GenreCreateView.as_view(),name='create_genre')
]
