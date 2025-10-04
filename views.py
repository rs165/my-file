from django.views import generic
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

class BookListView(generic.ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    paginate_by = 8

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(author__icontains=q)
        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'

class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'

class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
