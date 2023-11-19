from django.db.models import Avg, Min, Max, Count
from .models import Book, Author, Library
from .forms import BookForm
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    books = Book.objects.all()

    # Рассчитываем среднюю, минимальную и максимальную цены
    avg_price = books.aggregate(avg_price=Avg('price'))
    min_price = books.aggregate(min_price=Min('price'))
    max_price = books.aggregate(max_price=Max('price'))

    # Рассчитываем общее количество книг в библиотеке
    total_books = books.aggregate(total_books=Count('id'))

    authors = Author.objects.all()
    libraries = Library.objects.all()

    return render(request, 'library_app/index.html', {
        'books': books,
        'authors': authors,
        'libraries': libraries,
        'avg_price': avg_price['avg_price'],
        'min_price': min_price['min_price'],
        'max_price': max_price['max_price'],
        'total_books': total_books['total_books'],
    })

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()

    return render(request, 'library_app/add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm(instance=book)

    return render(request, 'library_app/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('index')

    return render(request, 'library_app/delete_book.html', {'book': book})