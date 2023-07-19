from django.shortcuts import render
from django.http import HttpResponse
from .models import BookData
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'books/home.html')


def book_list(request):
    book_object = BookData.objects.all()
    book_name = request.GET.get('book_name')
    if book_name != '' and book_name is not None:
        book_object = book_object.filter(name__icontains=book_name)

    paginator = Paginator(book_object, 5)
    page = request.GET.get('page')
    book_object = paginator.get_page(page)

    return render(request, 'books/book_list.html', {'book_object': book_object})


def book_detail(request, item_id):
    book = BookData.objects.get(pk=item_id)
    return render(request, 'books/details.html', {'book': book})


