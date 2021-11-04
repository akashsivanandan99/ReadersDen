from django.contrib import admin

# Register your models here.
from website.models import Author, Book, BookInstance, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
