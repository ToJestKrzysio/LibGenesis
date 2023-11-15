import uuid

from django.db import models
from django.contrib.auth import get_user_model


class UpdateTracerAbstractModel(models.Model):
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL, related_name="%(class)s_creations")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL, related_name="%(class)s_updates")

    class Meta:
        abstract = True


class Genre(UpdateTracerAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Author(UpdateTracerAbstractModel):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookSpec(UpdateTracerAbstractModel):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=200)
    publication_date = models.DateField(null=True, blank=True)
    no_pages = models.SmallIntegerField()
    max_borrow_time = models.SmallIntegerField()

    authors = models.ManyToManyField("Author", related_name="book_specs")
    genres = models.ManyToManyField("Genre",  related_name="book_specs")

    def __str__(self):
        return f"{self.title}"


class Book(UpdateTracerAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    spec = models.ForeignKey(BookSpec, null=True, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.spec.title}, id: {self.id}"


class Checkout(UpdateTracerAbstractModel):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    checked_at = models.DateTimeField(auto_now_add=True)
    return_before = models.DateTimeField()
    returned_at = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL, related_name="checkouts")
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name="checkouts")

    def __str__(self):
        was_returned = self.returned_at or 'not returned'
        return f"{self.book.spec.title} ({self.book.id}), borrowed: {self.checked_at}, returned: {was_returned}, return before: {self.return_before}"


class Reservation(UpdateTracerAbstractModel):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    valid_until = models.DateTimeField()
    completed = models.BooleanField(default=False)

    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL, related_name="reservations")
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name="reservations")

    def __str__(self):
        return f"{self.book.spec.title} ({self.book.id}), reserved: {self.created_at}, valid until: {self.valid_until}"