from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import BookForm, ReviewForm
from django.http import Http404
from django.db.models import Q
import requests

def index(req):
    """Returns the landing page"""
    path = "blrb_app/index.html"
    return render(req, path)

@login_required
def book_list(req):
    """List all user_added books"""
    books = Book.objects.filter(owner=req.user)
    path = "blrb_app/books.html"
    context = {'books':books}
    return render(req, path, context)

@login_required
def book(req, book_id):
    """List all user_added books"""
    book = Book.objects.get(id=book_id)

    if book.owner != req.user:
        raise Http404

    book_list = Book.objects.all()
    path = "blrb_app/book.html"
    context = {'book':book, 'book_list': book_list}
    return render(req, path, context)

@login_required
def new_book(req):
    if req.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(data=req.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.owner=req.user
            new_book.save()
            return redirect('blrb_app:book_list')
    path = "blrb_app/new_book.html"
    context={'form':form}
    return render(req, path, context)

@login_required
def new_review(req, book_id):
    """Add new review"""
    book = Book.objects.get(id=book_id)
    if req.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(data=req.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.book=book
            new_review.owner=req.user
            new_review.save()
            return redirect('blrb_app:book', book_id=book_id)
    path = "blrb_app/new_review.html"
    context = {'form': form, 'book': book }
    return render(req, path, context)

@login_required
def edit_review(req, book_id):
    """Edit existing reviews"""
    book = Book.objects.get(id=book_id)
    review = book.review

    if req.method != 'POST':
        form = ReviewForm(instance=review)
    else:
        form = ReviewForm(instance=review, data=req.POST)
        if form.is_valid():
            form.save()
            return redirect('blrb_app:book', book_id=book.id)
    path = "blrb_app/edit_review.html"
    context = {'book':book, 'review':review, 'form':form}
    return render(req, path, context)

@login_required
def delete_review(req, book_id):
    """Delete a review from a book"""
    book = Book.objects.get(id=book_id)
    review = book.review
    review.delete()
    return redirect('blrb_app:book', book_id=book.id)

@login_required
def delete_book(req, book_id):
    """Delete a book from a user's list"""
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('blrb_app:book_list')

def user_profile(req):
    """Render a personal page for each user"""
    books = Book.objects.all()
    context = {'books': books}
    path = 'blrb_app/user_profile.html'
    return render(req, path, context)

# Search filtering
def search(req):
    query = req.GET.get('q')
    path = 'blrb_app/search_results.html'
    if query:
        results = Book.objects.filter(Q(title__contains=query.strip()))
    else:
        results = Book.objects.all()
    context = {'search_results':results}
    return render(req, path, context)

# API for book selection/browsing
# def browse(req):
#     try :
#         browse_results = requests.get('')
#     except:
#         return browse_results.status_code
#     path = 'blrb_app/browse.html'
#     context = {'browse_results': browse_results}
#     return render(req, path, context)