from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('notes',views.notes, name='notes'),
    path('books', views.books, name='books'),
    path('notesDetails', views.notes_detail, name='notesDetails')
]