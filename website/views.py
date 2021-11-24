from django.shortcuts import render


# Create your views here.

def landing_view(request):
    return render(request, "index.html")


def test_view(request):
    return render(request, "about_us.html")
