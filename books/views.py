# Create your views here.
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Book, Student, Inventory
from django.db.models import Count
from rest_framework import serializers
from .serializers import BookSerializer, StudentSerializer, InventorySerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def perform_create(self, serializer):
        book_data = self.request.data.get('book')
        if book_data:
            book_serializer = BookSerializer(data=book_data)
            book_serializer.is_valid(raise_exception=True)
            book = book_serializer.save()
            serializer.save(book=book)
        else:
            raise serializers.ValidationError("Book data is required.")


class InventoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class IssueBookView(generics.UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def update(self, request, *args, **kwargs):
        inventory = self.get_object()
        if inventory.quantity == 0:
            raise ValidationError('Book not available')
        student_id = request.data.get('student_id')
        if Student.objects.get(id=student_id).books_issued.count() >= 3:
            raise ValidationError('Maximum books issued already')
        inventory.quantity -= 1
        inventory.save()
        student = Student.objects.get(id=student_id)
        student.books_issued.add(inventory)
        student.save()
        return super().update(request, *args, **kwargs)


class ReturnBookView(generics.UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def update(self, request, *args, **kwargs):
        inventory = self.get_object()
        student_id = request.data.get('student_id')
        student = Student.objects.get(id=student_id)
        student.books_issued.remove(inventory)
        student.save()
        inventory.quantity += 1
        inventory.save()
        return super().update(request, *args, **kwargs)


class PopularBooksView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Inventory.objects.annotate(num_borrowers=Count('student_set')).order_by('-num_borrowers')[:5].values(
            'book__title', 'num_borrowers')
