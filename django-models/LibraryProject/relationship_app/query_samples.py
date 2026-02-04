from relationship_app.models import Author, Book, Library

author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)

library = Library.objects.get(name="Main Library")
library_books = library.books.all()

librarian = library.librarian