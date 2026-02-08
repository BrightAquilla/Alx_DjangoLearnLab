# Create your models here.
from django.db import models
from relationship_app.models import Author

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]
class Author(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    


    def __str__(self):
        return self.title
