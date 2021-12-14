from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from website.models import Author


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
    return render(request, "components/add_book_form.html", context)
