from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from website.forms import AddBookForm
from website.models import Author, Book


def landing_view(request):
    return render(request, "index.html")


def test_view(request):
    return render(request, "components/add_book_form.html")


@login_required
def add_book_view(request):
    author = Author.objects.all()
    context = {
        'authors': author
    }

    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            title = form.cleaned_data['title']
            summary = form.cleaned_data['summary']
            isbn = form.cleaned_data['isbn']
            author = form.cleaned_data['author']
            book = Book()
    return render(request, "components/add_book_form.html", context)
