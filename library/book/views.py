from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book/list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context