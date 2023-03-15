from rest_framework import serializers
from .models import Book, Student, Inventory


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Inventory
        fields = ('book', 'quantity')
