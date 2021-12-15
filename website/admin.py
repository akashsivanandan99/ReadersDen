from django.contrib import admin

# Register your models here.
from website.models import Author, Book, BookInstance, Genre, CustomUser

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(CustomUser)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)

