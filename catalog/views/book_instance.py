from django.views import generic

from ..models.book_instance import BookInstance

class BookInstanceListView(generic.ListView):
    model = BookInstance
    context_object_name = 'book_instance_list'
    template_name = 'catalog/book_instance/book_instance_list.html'

class BookInstanceDetailtView(generic.DetailView):
    model = BookInstance
    context_object_name = 'book_instance_detail'
    template_name = 'catalog/book_instance/book_instance_detail.html'

class BookInstanceCreateView(generic.CreateView):
    model = BookInstance
    fields = [
        'unique_id',
        'due_back',
        'status',
        'imprint',
        'borrower'
    ]
    template_name = 'catalog/book_instance/book_instance_form.html'