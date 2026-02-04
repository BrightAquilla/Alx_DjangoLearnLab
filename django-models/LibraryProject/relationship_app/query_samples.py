from relationship_app.models import Author, Book, Library, Librarian

author_name = 'John Doe'
author = Author.objects.get(name= author_name)
books_by_author = Book.objects.filter(author=author)

library_name= 'Central Library'
library = Library.objects.get(name=library_name)
library_books = library.books.all()


librarian = Librarian.objects.get(library=library)