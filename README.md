# Books_Inventory_Management_System

Design and create a backend using Django rest framework API’s of a small application of books
inventory management system which has the following features.

1. New Books can be added , updated and deleted (CRUD).
2. New Readers can be added and deleted.
3. Reader can issue book for Reading and return them.
4. A Reader can only have 3 books a time
5. HTTP 400’s in case of exception/error. For example if a student requesting a book that is not
available in the library or inventory is 0 for a book.
6. Getting information of Books issued by a reader with proper details.

Additional points for:
Creating an API endpoint which will give us 5 popular books among students along with the
number of times they were issued.

Must have tables:
1. Books
2. Students
3. Inventory (for Books)
There can be additional tables Also.
