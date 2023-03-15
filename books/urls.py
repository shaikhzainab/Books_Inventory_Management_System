
from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView, \
                   StudentListCreateView, StudentRetrieveUpdateDeleteView, \
                   InventoryListCreateView, InventoryRetrieveUpdateDeleteView, \
                   IssueBookView, ReturnBookView, PopularBooksView

urlpatterns = [
    # gives the list of books
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

    # gives the detail of books using ID
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),

    # gives the list of students/readers
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),

    # gives the list of students/readers
    path('students/<int:pk>/', StudentRetrieveUpdateDeleteView.as_view(), name='student-retrieve-update-delete'),

    # gives the list of books avlbl in the inventory
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),

    # gives the detail of books avlbl in the inventory using ID
    path('inventory/<int:pk>/', InventoryRetrieveUpdateDeleteView.as_view(), name='inventory-retrieve-update-delete'),

    # gives the detail of issued books
    path('issue-book/<int:pk>/', IssueBookView.as_view(), name='issue-book'),

    # gives the detail of books which are retured by the student
    path('return-book/<int:pk>/', ReturnBookView.as_view(), name='return-book'),

    # gives the detail of pupular books  condition ( 5 most issued books comes under popular books)
    path('popular-books/', PopularBooksView.as_view(), name='popular-books'),
]