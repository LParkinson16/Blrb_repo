"""Custom url paths for the Blrb app"""

from django.urls import path
from . import views

app_name = 'blrb_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>', views.book, name='book'),
    # path('review/', views.review, name='review')
    path('new_book/', views.new_book, name='new_book'),
    path('new_review/<int:book_id>', views.new_review, name='new_review'),
    path('edit_review/<int:book_id>', views.edit_review, name='edit_review'),
    path('delete_review/<int:book_id>', views.delete_review, name='delete_review'),
    path('delete_book/<int:book_id>', views.delete_book, name='delete_book'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('search/', views.search, name='search'),
    # API integration
    path('browse/', views.browse, name='browse_books'),
]