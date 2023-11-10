from rest_framework import viewsets

from . import models, serializers


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AuthorSerializer
    queryset = models.Book.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GenreSerializer
    queryset = models.Book.objects.all()
