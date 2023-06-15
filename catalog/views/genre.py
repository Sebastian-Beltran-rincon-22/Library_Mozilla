from django.views import generic

from ..models.genre import Genre


class GenreListView(generic.ListView):
    model = Genre
    context_object_name = 'genre_list'
    template_name = 'catalog/genre/genre_list.html'

class GenreDetailtView(generic.DetailView):
    model = Genre
    context_object_name = 'genre_detail'
    template_name = 'catalog/genre/genre_detail.html'

class GenreCreateView(generic.CreateView):
    model = Genre
    fields = [
        'name',
    ]
    template_name = 'catalog/genre/genre_form.html'

