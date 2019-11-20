from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy

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


class BookCreateView(CreateView):
    model = Book
    template_name = 'book/create.html'
    fields = ('name', 'pages', 'isbn_number')
    success_url = reverse_lazy('book-list')

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'
    context_object_name = 'book'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book/update.html'
    context_object_name = 'book'
    fields = ('name', 'pages', 'isbn_number',)
    # success_url = reverse_lazy('book-list')

    def get_success_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.object.id})

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = reverse_lazy('book-list')