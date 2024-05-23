from django.contrib import admin

from .models import Author, Book, Genre

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_date']

admin.site.register(Author, AuthorAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Genre, GenreAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'genre', 'publication_date']

admin.site.register(Book, BookAdmin)