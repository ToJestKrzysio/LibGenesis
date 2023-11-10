import uuid

from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200, null=False, blank=False)
    authors = models.ManyToManyField("Author")
    genres = models.ManyToManyField("Genre")
    publication_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} - {self.publication_date.year}"


class Genre(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
