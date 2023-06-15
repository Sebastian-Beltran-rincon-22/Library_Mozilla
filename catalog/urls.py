from django.urls import path

from .views import views
from .views import author
from .views import book_instance

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