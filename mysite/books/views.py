from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.shortcuts import render
from .models import Book, Author

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'authors/author_detail.html', {'author': author, 'books': books})
