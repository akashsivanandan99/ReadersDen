from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from website.forms import AddBookForm
from website.models import Author, Book, Genre


def landing_view(request):
    return render(request, "index_new.html")


def test_view(request):
    return render(request, "components/add_book_form.html")


@login_required
def add_book_view(request):
    authors = Author.objects.all()
    genres = Genre.objects.all()
    context = {
        'authors': authors,
        'genres': genres,
    }

    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            print("Form valid")
            title = form.cleaned_data['title']
            summary = form.cleaned_data['summary']
            isbn = form.cleaned_data['isbn']
            author = Author.objects.get(id=form.cleaned_data['author'])
            print(author.name)
            genre = Genre.objects.get(id=form.cleaned_data['genre'])
            book = Book(title=title, summary=summary, isbn=isbn)
            book.author = author
            print(form.__dict__)
            book.save()
            book.genre.set(form.cleaned_data['genre'])
            book.save()
        else:
            print(form.errors)
    return render(request, "components/add_book_form.html", context)
