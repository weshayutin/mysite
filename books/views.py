# Create your views here.
from django.shortcuts import render_to_response, HttpResponse
from books.models import Book, Author, AuthorForm
from django.http import HttpResponseRedirect
from django import forms
from django.core.mail import send_mail
from django.forms.models import modelformset_factory
from django.shortcuts import render


def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return render_to_response('book/search_form.html')
    

def add(request):
    if request.POST and request.POST['name']:
        form = Book(request.POST)
        if form.is_valid():
            form.save()
    else:
        return render_to_response('book/add_book.html')

def manage_authors_formset(request):
    AuthorFormSet = modelformset_factory(Author)
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = AuthorFormSet()
    return render_to_response('book/manage_books_formset.html', {
        "formset": formset,
    })
    
def manage_authors_form(request):
    if request.method == 'POST': # If the form has been submitted...
        form = AuthorForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = AuthorForm() # An unbound form

    return render(request, 'book/manage_books_form.html', {
        'form': form,
    })