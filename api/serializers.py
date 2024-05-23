from rest_framework import serializers

from .models import Author, Book, Genre


class AuthorSerializer(serializers.ModelSerializer):
    my_name_field = serializers.CharField(read_only=True, default='Ali')

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'my_name_field']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'publication_date']
