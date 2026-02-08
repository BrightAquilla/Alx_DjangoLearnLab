from django.urls import path
from .views import admin_view
from .views import librarian_view
from .views import member_view
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView
from .views import add_book, edit_book, delete_book
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    list_books,
    LibraryDetailView,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:pk>/', edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),
    
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/templates/relationship_app/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/templates/relationship_app/logout.html'), name='logout'),
    path('register/',views.register, name='register'),

    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),

    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),

]
