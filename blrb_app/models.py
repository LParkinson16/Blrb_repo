from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    """Instance of a book to be reviewed by a user"""
    title = models.CharField(max_length=60)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # *WIP on loading the next book in query set

    # ordering = models.PositiveSmallIntegerField()
    # class Meta():
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=["module", "ordering"], name="book_order"
    #         )
    #     ]
   
    def __str__(self):
        """Return string representation of this model"""
        return self.title
    

    # def get_next_book(self):
    #     """Cycle to the next book in the list"""
    #     next_book_index = self.ordering+1
    #     next_book = Book.objects.filter(module = self.module, ordering = next_book_index).first()
    #     return next_book
    
    # def get_previous_book(self):
    #     """Cycle to the next book in the list"""
    #     previous_book_index = self.ordering-1
    #     previous_book = Book.objects.filter(module = self.module, ordering = previous_book_index).first()
    #     return previous_book


class Review(models.Model):
    """A singular review belonging to an associated book"""
    content = models.CharField()
    tagline = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        """Return string representation of this model"""
        return self.content
