from django.urls import path

from .views import views
from .views import author

urlpatterns = [
    path('',views.index,name="index") 
]

urlpatterns += [
    path("author",author.AuthorListView.as_view(),name="author"),
    path("author/<int:pk>",author.AuthorDetailView.as_view(),name='author_detail'),
    path("author/create",author.AuthorCreateView.as_view(),name='create_author')
]
