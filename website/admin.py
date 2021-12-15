from django.contrib import admin

# Register your models here.
from website.models import Author, Book, BookInstance, Genre, CustomUser, Contact

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(CustomUser)
admin.site.register(Contact)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
