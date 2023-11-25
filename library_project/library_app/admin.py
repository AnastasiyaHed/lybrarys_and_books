from django.contrib import admin
from .models import Library, Author, Book


class LibraryAdmin(admin.ModelAdmin):
     list_display = ('location', 'established_date')  # Отображаем название и город библиотеки


class AuthorAdmin(admin.ModelAdmin):
     list_display = ('name', 'birth_date', 'nationality')  # Отображаем имя автора


class BookAdmin(admin.ModelAdmin):
     list_display = ('author', 'library')  # Отображаем название, автора и библиотеку книги


admin.site.register(Library, LibraryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

