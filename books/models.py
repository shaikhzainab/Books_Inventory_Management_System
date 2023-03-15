from django.db import models


# Book model contains information about the books available in the library
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)


# Student model contains information about the library users
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    books_issued = models.ManyToManyField('Inventory', related_name='borrowers')


# Inventory model represents the stock of books available in the library
class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
