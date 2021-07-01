from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    return render(request, 'dashboard/notes.html')

def books(request):
    return render(request, 'dashboard/books.html')

def notes_detail(request):
    return render(request, 'dashboard/notes_detail.html')