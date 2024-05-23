from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=191)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=191)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=191)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    

    