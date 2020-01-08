from django.shortcuts import render

# Create your views here.


def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def about(request):
    """View to display about.html"""
    return render(request, "about.html")
